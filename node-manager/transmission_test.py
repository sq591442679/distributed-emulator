"""
added by sqsq
used for LoFi test
"""
from multiprocessing import Process, Queue
import typing
import re
from scapy.all import sniff, UDP, IP
import time
import json
import subprocess

from loguru import logger
from const_var import *
from docker_client import DockerClient
from global_var import network_dict
from tools import *


receiver_port = 12345
receiver_ip = ""
total_data_bytes = 0
total_control_bytes = 0

"""
find ONE ip address of a certain satellite node
"""
def get_ip_of_node_id(docker_client: DockerClient, node_id: tuple) -> str:
    for network in network_dict.values():
        for container_name in network.inner_eth_dict.keys():
            container = docker_client.client.containers.get(container_name)
            container_node_id = satellite_str_to_id_tuple(container.name)
            if container_node_id == node_id:
                ret = docker_client.exec_cmd(container_name, "ip addr show eth1")
                if ret[0] != 0:
                    logger.error(ret[1].decode().strip())
                else:
                    result = ret[1].decode().strip()
                    match = re.search(r'inet\s+(\d+\.\d+\.\d+\.\d+)', result)
                    if match:
                        logger.success(f"found ip: {match.group(1)}")
                        return match.group(1)
                    else:
                        logger.error("ip address not found")
    raise Exception(f"node id {node_id} not found")
                

"""
shared_result_list: list[dict]
"""
def start_udp_receiver(docker_client: DockerClient, send_interval: float, shared_result_list) -> None:
    logger.info("UDP receiver starting")
    receiver_node_name = satellite_id_tuple_to_str(RECEIVER_NODE_ID)
    expected_recv_cnt = int(SIMULATION_DURATION / send_interval * len(SENDER_NODE_ID_LIST))
    ret = docker_client.exec_cmd(receiver_node_name, 
                                 f"python3 /udp-applications/udp_receiver.py "
                                 f"{receiver_ip} {receiver_port} {SIMULATION_DURATION} "
                                 f"{SIMULATION_DURATION + 10} {expected_recv_cnt}")
    if ret[0] != 0:
        logger.error(ret[1].decode().strip())
    else:
        line = ret[1]
        if len(line.decode().strip()) > 0:
            # logger.info(line.decode().strip())
            shared_result_list.append(json.loads(line.decode().strip()))


def start_udp_sender(sender_node_id: tuple, docker_client: DockerClient, send_interval: float) -> None:
    sender_node_name = satellite_id_tuple_to_str(sender_node_id)
    logger.info(f"UDP sender {sender_node_name} starting, dst:{receiver_ip}:{receiver_port}")
    ret = docker_client.exec_cmd(sender_node_name,
                                 f"python3 /udp-applications/udp_sender.py "
                                 f"{receiver_ip} {receiver_port} {send_interval} {SIMULATION_DURATION}")
    

"""
shared_result_list: list[dict]
"""
def start_transmission_test(docker_client: DockerClient, send_interval: float, shared_result_list):
    global receiver_ip

    os.system("dmesg -c > /dev/null")

    receiver_ip = get_ip_of_node_id(docker_client, RECEIVER_NODE_ID)
    process_list: typing.List[Process] = []
    
    process_receiver = Process(target=start_udp_receiver, args=(docker_client, send_interval, shared_result_list))
    process_list.append(process_receiver)
    for sender_node_id in SENDER_NODE_ID_LIST:
        process_sender = Process(target=start_udp_sender, args=(sender_node_id, docker_client, send_interval))
        process_list.append(process_sender)

    for process in process_list:
        process.start()
    for process in process_list:
        process.join()

    expected_recv_cnt = int(SIMULATION_DURATION / send_interval * len(SENDER_NODE_ID_LIST))
    os.system("rmmod packet_drop_module")   # need to uninstall here to get drop cnt
    commands = ["dmesg | grep 'ttl exceed packet cnt:'", "dmesg | grep 'no entry packet cnt:'"]
    result_keys = ['ttl_drop_ratio', 'no_entry_ratio']
    for i in range(len(commands)):
        command = commands[i]
        result_key = result_keys[i]
        output = subprocess.check_output(command, shell=True, text=True)
        drop_cnt = int(output.split(':')[-1].strip())
        drop_ratio = drop_cnt / expected_recv_cnt
        shared_result_list.append({result_key: "%.1f%%" % (drop_ratio * 100)})

    # logger.info(shared_result_list)

    # logger.success("UDP send and receive completed")
    # return (shared_result_list, ttl_drop_ratio)


def get_all_interfaces():
    with open("/proc/net/dev") as file:
        lines = file.readlines()[2:]
        return [re.split(r'\s*:\s*', line)[0] for line in lines]


def packet_capture_callback(packet):
    global total_data_bytes, total_control_bytes
    if UDP in packet and packet[UDP].dport == receiver_port:
        udp_packet = packet[UDP].load
        total_data_bytes += len(udp_packet)
    elif IP in packet and packet[IP].proto == 89:  # Check for OSPF LSU (type=4)
        ospf_packet = packet[IP].load
        ospf_packet_type = ospf_packet[1] if len((ospf_packet)) > 1 else None
        if (ospf_packet_type == 4):
            # logger.info(ospf_packet)
            total_control_bytes += len(ospf_packet)

"""
returns data throughput and control overhead
unit: MBps
"""
def start_packet_capture(queue: Queue):
    start_time = time.time()
    interfaces = [interface for interface in get_all_interfaces() if interface.startswith('veth')]

    logger.info(f'sniffing on {interfaces}')

    try:
        while time.time() - start_time <= SIMULATION_DURATION:
            sniff(prn=packet_capture_callback, filter="udp dst port 12345 or ip proto 89", 
                iface=interfaces, store=0, timeout=1)
    except KeyboardInterrupt:
        pass
    
    res_dict = {}
    res_dict["throughput"] = "%.6f" % (total_data_bytes / 1e6 / SIMULATION_DURATION)
    res_dict["control overhead"] = "%.6f" % (total_control_bytes / 1e6 / SIMULATION_DURATION)

    queue.put(res_dict)

"""
added by sqsq
used for LoFi test
"""
from multiprocessing import Manager, Process
import typing
import re
from loguru import logger
from const_var import *
from docker_client import DockerClient
from global_var import network_dict
from tools import *


receiver_port = 12345
receiver_ip = ""

"""
find ONE ip address of a certain satellite node
"""
def get_ip_of_node_id(docker_client: DockerClient, node_id: tuple) -> str:
    for network in network_dict.values():
        for container_id in network.veth_map.keys():
            container = docker_client.client.containers.get(container_id)
            container_node_id = satellite_str_to_id_tuple(container.name)
            if container_node_id == node_id:
                grep_command = "grep -oP \"(?<=inet\\s)\\d+(\\.\\d+){3}\""
                ret = container.exec_run(f"ip addr show eth1")
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
                

def start_udp_receiver(docker_client: DockerClient, send_interval: float, shared_result_list) -> None:
    
    receiver_node_name = satellite_id_tuple_to_str(RECEIVER_NODE_ID)
    receiver_container = docker_client.client.containers.get(receiver_node_name)
    ret = receiver_container.exec_run(f"python3 /udp-applications/udp_receiver.py "
                                      f"{receiver_ip} {receiver_port} "
                                      f"{SIMULATION_END_TIME + 10} {int(SIMULATION_END_TIME / send_interval * len(SENDER_NODE_ID_LIST))}",
                                stream=True)
    logger.success("UDP receiver started")

    for line in ret[1]:
        if len(line.decode().strip()) > 0:
            shared_result_list.append(line.decode().strip())
            logger.info(line.decode().strip())


def start_udp_sender(sender_node_id: tuple, docker_client: DockerClient, send_interval: float) -> None:
    sender_node_name = satellite_id_tuple_to_str(sender_node_id)
    sender_container = docker_client.client.containers.get(sender_node_name)
    ret = sender_container.exec_run(f"python3 /udp-applications/udp_sender.py "
                                    f"{receiver_ip} {receiver_port} {send_interval} {SIMULATION_END_TIME}",
                                    stream=True)
    logger.success(f"UDP sender {sender_node_name} started")


def start_transmission_test(docker_client: DockerClient, send_interval: float):
    global receiver_ip
    receiver_ip = get_ip_of_node_id(docker_client, RECEIVER_NODE_ID)

    manager = Manager()
    shared_result_list = manager.list()

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
    
    logger.success("UDP send and receive completed")
    return shared_result_list


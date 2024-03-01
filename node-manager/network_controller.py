import time
from multiprocessing import Process, Lock
from multiprocessing.connection import Pipe
from loguru import logger
import os
from math import cos, sin, sqrt
from typing import Dict, List, Tuple
from const_var import *
from satellite_node import SatelliteNode
from global_var import network_dict,satellite_map
from threading import Thread
from tools import *
import random
from docker_client import DockerClient
from typing import Dict, List

def generate_submission_list_for_network_object_creation(missions, submission_size: int):
    submission_list = []
    for i in range(0, len(missions), submission_size):
        submission_list.append(missions[i:i + submission_size])
    return submission_list


def network_object_creation_submission(docker_client, submission, send_pipe):
    for net_id, container_id1, container_id2 in submission:
        network_key = get_network_key(container_id1, container_id2)
        network_dict[network_key] = Network(docker_client,
                                        net_id,
                                        container_id1,
                                        container_id2,
                                        NETWORK_DELAY,
                                        NETWORK_BANDWIDTH,
                                        NETWORK_LOSS,
                                        QUEUE_CAPACITY)
        # print(network_key)
    send_pipe.send("finished")


def create_network_object_with_multiple_process(docker_client, missions, submission_size):
    current_finished_submission_count = 0
    rcv_pipe, send_pipe = Pipe()
    submission_list = generate_submission_list_for_network_object_creation(missions, submission_size)
    # logger.info(f"create_network_object_submission_size: {submission_size}")
    for single_submission in submission_list:
        singleThread = Thread(target=network_object_creation_submission, args=(docker_client, single_submission, send_pipe))
        singleThread.start()
    while True:
        rcv_string = rcv_pipe.recv()
        if rcv_string == "finished":
            current_finished_submission_count += 1
            if current_finished_submission_count == len(submission_list):
                rcv_pipe.close()
                send_pipe.close()
                break


def get_laser_delay_ms(position1: dict, position2: dict) -> int:
    lat1, lon1, hei1 = position1[LATITUDE_KEY], position1[LONGITUDE_KEY], position1[HEIGHT_KEY]
    lat2, lon2, hei2 = position2[LATITUDE_KEY], position2[LONGITUDE_KEY], position2[HEIGHT_KEY]
    x1, y1, z1 = hei1 * cos(lat1) * cos(lon1), hei1 * cos(lat1) * sin(lon1), hei1 * sin(lat1)
    x2, y2, z2 = hei2 * cos(lat2) * cos(lon2), hei2 * cos(lat2) * sin(lon2), hei2 * sin(lat2)
    dist_square = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2  # UNIT: m^2
    # logger.info(f"distance: {int(sqrt(dist_square))} light speed: {LIGHT_SPEED}")
    # return int(sqrt(dist_square) / LIGHT_SPEED)  # UNIT: ms
    # ZHF MODIFY
    return 0


def get_network_key(container_id1: str, container_id2: str) -> str:
    if container_id1 > container_id2:
        container_id1, container_id2 = container_id2, container_id1
    return container_id1 + container_id2


class ContainerEntrypoint:
    def __init__(self, veth_name: str, container_id: str):
        self.veth_name = veth_name
        self.container_id = container_id


def get_bridge_interface_name(bridge_id: str) -> str:
    full_name = "br-" + bridge_id
    br_interfaces_str = os.popen(
        '''ip l | grep -e "br-" | awk 'BEGIN{FS=": "}{print $2}' ''').read()  # popen与system可以执行指令,popen可以接受返回对象
    interface_list = br_interfaces_str.split('\n')[:-1]
    for interface_name in interface_list:
        if full_name.startswith(interface_name, 0):
            return interface_name
    raise SystemError("Interface Not Found")


def get_vethes_of_bridge(interface_name: str) -> list:
    command = "ip l | " \
              "grep -e \"veth\" | " \
              "grep \"%s\" | " \
              "awk \'BEGIN{FS=\": \"}{print $2}\' | " \
              "awk \'BEGIN{FS=\"@\"}{print $1}\'" % interface_name
    veth_list_str = os.popen(command).read()
    veth_list = veth_list_str.split("\n")[:-1]
    return veth_list



def get_inner_eth_dict(container_id_list: List[str], veth_list: List[str], docker_client: DockerClient) -> List[Dict[str, str]]:
    """
    added by sqsq
    e.g., for a veth3dr431, find it corresponds to eth3 in node_1_1
    return: list of dict, 
    veth_dict: container_name(str) -> outer veth name of the corresponding network
    eth_dict: container_name(str) -> inner eth name of the container which connects to the corresponding network 
    note that the mapping of container_id and veth_name is uncertain
    """    
    veth_dict: Dict[str, str] = {}
    eth_dict: Dict[str, str] = {}
    for container_id in container_id_list:
        container_name = docker_client.client.containers.get(container_id).name
        ret = docker_client.exec_cmd(container_id, 'ls /sys/class/net/')
        if ret[0] != 0:
            logger.error(ret[1].decode().strip())
            raise Exception('get_inner_eth_dict failed')
        eth_names = ret[1].decode().strip().split('\n')
        # logger.info(eth_names)

        for veth_name in veth_list:
            iflink: str = os.popen(f"cat /sys/class/net/{veth_name}/iflink").read().strip()
            for eth_name in eth_names:
                command = f"cat /sys/class/net/{eth_name}/ifindex"
                ret = docker_client.exec_cmd(container_id, command)
                if ret[0] != 0:
                    logger.error(ret[1].decode().strip())
                    raise Exception('get_inner_eth_dict failed')
                else:
                    if ret[1].decode().strip() == iflink:
                        eth_dict[container_name] = eth_name
                        veth_dict[container_name] = veth_name
                        break
            # if container_name not in ret_dict.keys():
            #     logger.error(f"{container_name} has no inner eth corresponds to {veth_name}")
            #     raise Exception(f"{container_name} has no inner eth corresponds to {veth_name}")
    
    if len(set(veth_dict.values())) != 2 or len(veth_dict.keys()) != 2:
        logger.error(f"veth_dict: {veth_dict}, eth_dict: {eth_dict}")
        raise Exception("bad ret_dict")

    # logger.info(f"veth_dict: {veth_dict}, eth_dict: {eth_dict}")

    return [veth_dict, eth_dict]


class Network:

    def __init__(self,
                 docker_client: DockerClient,
                 bridge_id: str,
                 container_id1: str,
                 container_id2: str,
                 time: int,
                 band_width: str,
                 loss_percent: int,
                 queue_capacity: int):
        # 为保证network key的唯一性，设置map中key的字符串拼接顺序为小id在前,大id在后
        self.docker_client = docker_client
        self.br_id = bridge_id
        self.br_interface_name = get_bridge_interface_name(bridge_id)
        self.veth_interface_list = get_vethes_of_bridge(self.br_interface_name)
        self.delay = time               # unit: ms
        self.bandwidth = band_width     # '10Mbit'
        self.loss = loss_percent        # unit: percent
        self.queue_capacity = queue_capacity
        if len(self.veth_interface_list) != 2:
            logger.warning(self.veth_interface_list)
            raise ValueError("wrong veth number of bridge: %d" % len(self.veth_interface_list))
        
        # added by sqsq
        self.veth_dict, self.inner_eth_dict = get_inner_eth_dict([container_id1, container_id2], 
                                                                 self.veth_interface_list, 
                                                                 self.docker_client)

        # added by sqsq
        self.is_down = False    # if True, then do not really update info
        self.down_momnet = 0.0

        self.init_info()

    '''
    #!/bin/bash
    echo "add tbf and netem to eth0..."
    tc qdisc del dev eth0 root
    tc qdisc add dev eth0 root handle 1:0 tbf rate 80kbit burst 10k limit 10kbit
    tc qdisc add dev eth0 parent 2:0 handle 1:0 netem delay 100ms loss 10%
    tc qdisc show dev eth0
    '''
    def init_info(self):
        for container_name, inner_eth_name in self.inner_eth_dict.items():
            command = f'tc qdisc add dev {inner_eth_name} root netem delay {self.delay}ms rate {self.bandwidth} limit {self.queue_capacity}'
            self.docker_client.exec_cmd(container_name, command)

    def update_info(self):
        for container_name, inner_eth_name in self.inner_eth_dict.items():
            command = f'tc qdisc replace dev {inner_eth_name} root netem delay {self.delay}ms rate {self.bandwidth} limit {self.queue_capacity}'
            self.docker_client.exec_cmd(container_name, command)

    def update_delay_param(self, set_time: int):
        self.delay = set_time
        if not self.is_down:
            self.update_info()

    def update_bandwidth_param(self, band_width: str):
        self.bandwidth = band_width
        if not self.is_down:
            self.update_info()

    def update_loss_param(self, loss_percent: str):
        self.loss = loss_percent
        if not self.is_down:
            self.update_info()

    # added by sqsq
    def close_link(self, sim_time: float = None):
        self.is_down = True
        for container_name, eth_name in self.inner_eth_dict.items():
            command = f"ifconfig {eth_name} down"
            self.docker_client.exec_cmd(container_name, command)

        if sim_time is not None:
            container_name_list = list(self.inner_eth_dict.keys())
            logger.info(
                '{"sim_time": %.3f, "link": "%s <--> %s", "type": "down"}'
                % (sim_time, container_name_list[0], container_name_list[1])
            )

    def open_link(self, sim_time:float = None):
        for container_id, eth_name in self.inner_eth_dict.items():
            command = f"ifconfig {eth_name} up"
            self.docker_client.exec_cmd(container_id, command)
        self.is_down = False
        self.update_info()

        if sim_time is not None:
            container_name_list = list(self.inner_eth_dict.keys())
            logger.info(
                '{"sim_time": %.3f, "link": "%s <--> %s", "type": "up"}'
                % (sim_time, container_name_list[0], container_name_list[1])
            )


"""
added by sqsq
for link failure generating
"""
def generate_link_failure(docker_client: DockerClient, link_failure_rate: float):
    if abs(link_failure_rate - 0) < 1e-6:
        return
    
    lock = Lock()

    poisson_lambda = link_failure_rate / (LINK_FAILURE_DURATION * (1 - link_failure_rate))
    start_time = time.time()

    for network in network_dict.values():   # generate first down moment
        sim_time_interval = random.expovariate(poisson_lambda)
        network.down_moment = sim_time_interval
    
    flag = False
    while True:
         if (flag):
             break
         for network in network_dict.values():

            current_sim_time = time.time() - start_time

            if current_sim_time <= SIMULATION_DURATION:
                if network.is_down and current_sim_time <= network.down_moment + LINK_FAILURE_DURATION:
                    # link is in down state
                    continue
                elif network.is_down and current_sim_time > network.down_moment + LINK_FAILURE_DURATION:
                    # link should recover
                    with lock:
                        network.open_link(current_sim_time)
                    sim_time_interval = random.expovariate(poisson_lambda)
                    network.down_moment = current_sim_time + sim_time_interval # set the next link down moment
                elif not network.is_down and current_sim_time > network.down_moment:
                    # link should turned to down
                    with lock:
                        network.close_link(current_sim_time)
                else:
                    continue

                current_sim_time = time.time() - start_time
                if current_sim_time >= SIMULATION_DURATION:
                    break
            else:   # sim time exceeded, loop should stop
                flag = True  


def generate_mission_for_update_network_delay(position_data: Dict[str, Dict[str, float]], topo: Dict[str, List[str]],
                                              satellite_map_tmp: Dict[str, SatelliteNode]):
    update_network_delay_missions = []
    for start_node_id in topo.keys():
        conn_array = topo[start_node_id]
        for target_node_id in conn_array:
            start_container_id = satellite_map_tmp[start_node_id].container_id
            target_container_id = satellite_map_tmp[target_node_id].container_id
            start_node_id_str = satellite_id_tuple_to_str(start_node_id)
            target_node_id_str = satellite_id_tuple_to_str(target_node_id)
            delay = get_laser_delay_ms(position_data[start_node_id_str], position_data[target_node_id_str])
            network_key = get_network_key(start_container_id, target_container_id)
            update_network_delay_missions.append(
                (network_key, delay)
            )
    return update_network_delay_missions

def update_network_delay(position_data: dict, topo: dict):
    for start_node_id in topo.keys():
        conn_array = topo[start_node_id]
        for target_node_id in conn_array:
            start_node_id_str = satellite_id_tuple_to_str(start_node_id)
            target_node_id_str = satellite_id_tuple_to_str(target_node_id)
            delay = get_laser_delay_ms(position_data[start_node_id_str],position_data[target_node_id_str])
            start_container_id = satellite_map[start_node_id].container_id
            target_container_id = satellite_map[target_node_id].container_id
            net_object = network_dict[get_network_key(start_container_id,target_container_id)]
            net_object.update_delay_param(delay)


def generate_submission_list_for_update_network_delay(missions: List[Tuple[str, int]],
                                                      submission_size: int):
    submission_list = []
    for i in range(0, len(missions), submission_size):
        submission_list.append(missions[i:i + submission_size])
    return submission_list


def update_network_delay_with_single_process(submission: List[Tuple[str, int]], networks_tmp, send_pipe):
    for network_key, delay in submission:
        network = networks_tmp[network_key]
        network.update_delay_param(delay)
    send_pipe.send("finished")


def update_network_delay_with_multi_process(stop_process_state,
                                            networks_tmp,
                                            position_data: Dict[str, Dict[str, float]],
                                            topo: Dict[str, List[str]],
                                            satellite_map_tmp: Dict[str, SatelliteNode],
                                            submission_size: int,
                                            update_interval: int):
    # update count
    update_count = 0
    # generate missions
    missions = generate_mission_for_update_network_delay(position_data, topo, satellite_map_tmp)
    # generate submission list
    submission_list = generate_submission_list_for_update_network_delay(missions, submission_size)
    # submit
    while True:
        # store the start time
        start_time = time.time()
        if stop_process_state.value:
            break
        # current count
        current_count = 0
        # generate pipe
        rcv_pipe, send_pipe = Pipe()
        for submission in submission_list:
            # process = Process(target=update_network_delay_with_single_process,
            #                   args=(submission, networks_tmp, send_pipe))
            # process.start()
            singleThread = Thread(target=update_network_delay_with_single_process,
                                  args=(submission, networks_tmp, send_pipe))
            singleThread.start()
        # receive the result
        while True:
            rcv_string = rcv_pipe.recv()
            if rcv_string == "finished":
                current_count += 1
                # traverse all the process and kill them
                if current_count == len(submission_list):
                    send_pipe.close()
                    rcv_pipe.close()
                    break
        end_time = time.time()
        logger.info(f"update satellite network delay in {end_time - start_time}s")
        update_count += 1
        if update_count == 1:
            break
        time.sleep(update_interval)
    logger.success("update satellite network delay process finished")


if __name__ == '__main__':
    print(generate_submission_list_for_network_object_creation([1, 2, 3, 4, 5], 1))

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

def generate_submission_list_for_network_object_creation(missions, submission_size: int):
    submission_list = []
    for i in range(0, len(missions), submission_size):
        submission_list.append(missions[i:i + submission_size])
    return submission_list


def network_object_creation_submission(submission, send_pipe):
    for net_id, container_id1, container_id2 in submission:
        network_key = get_network_key(container_id1, container_id2)
        network_dict[network_key] = Network(net_id,
                                        container_id1,
                                        container_id2,
                                        NETWORK_DELAY,
                                        NETWORK_BANDWIDTH,
                                        NETWORK_LOSS)
        # print(network_key)
    send_pipe.send("finished")


def create_network_object_with_multiple_process(missions, submission_size):
    current_finished_submission_count = 0
    rcv_pipe, send_pipe = Pipe()
    submission_list = generate_submission_list_for_network_object_creation(missions, submission_size)
    # logger.info(f"create_network_object_submission_size: {submission_size}")
    for single_submission in submission_list:
        singleThread = Thread(target=network_object_creation_submission, args=(single_submission, send_pipe))
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


class Network:

    def __init__(self,
                 bridge_id: str,
                 container_id1: str,
                 container_id2: str,
                 time: int,
                 band_width: str,
                 loss_percent: str):
        # 为保证network key的唯一性，设置map中key的字符串拼接顺序为小id在前,大id在后
        self.br_id = bridge_id
        self.br_interface_name = get_bridge_interface_name(bridge_id)
        self.veth_interface_list = get_vethes_of_bridge(self.br_interface_name)
        self.delay = time
        self.bandwidth = band_width
        self.loss = loss_percent
        if len(self.veth_interface_list) != 2:
            logger.warning(self.veth_interface_list)
            raise ValueError("wrong veth number of bridge: %d" % len(self.veth_interface_list))
        self.veth_map = {
            container_id1: self.veth_interface_list[0],
            container_id2: self.veth_interface_list[1]
        }

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
        # bandwidth unit is kbytes/s integer
        command = "tc qdisc replace dev %s root handle 1:0 tbf rate %dkbit burst %dk limit %dkbit" % (
            self.veth_interface_list[0], self.bandwidth*8, self.bandwidth, self.bandwidth*8)
        exec_res = os.popen(command).read()
        
        command = "tc qdisc add dev %s parent 1:0 handle 2:0 netem delay %dms loss %s" % (
            self.veth_interface_list[0], self.delay, self.loss)
        exec_res = os.popen(command).read()

        # bandwidth unit is kbytes/s integer
        command = "tc qdisc replace dev %s root handle 1:0 tbf rate %dkbit burst %dk limit %dkbit" % (
            self.veth_interface_list[1], self.bandwidth*8, self.bandwidth, self.bandwidth*8)
        exec_res = os.popen(command).read()

        command = "tc qdisc add dev %s parent 1:0 handle 2:0 netem delay %dms loss %s" % (
            self.veth_interface_list[1], self.delay, self.loss)
        exec_res = os.popen(command).read()

    def update_info(self):
        command = "tc qdisc replace dev %s root handle 1:0 tbf rate %dkbit burst %dk limit %dkbit" % (
            self.veth_interface_list[0], self.bandwidth*8, self.bandwidth, self.bandwidth*8)
        
        exec_res = os.popen(command).read()
        command = "tc qdisc replace dev %s parent 1:0 handle 2:0 netem delay %dms loss %s" % (
            self.veth_interface_list[0], self.delay, self.loss)
        
        exec_res = os.popen(command).read()
        # bandwidth unit is kbytes/s integer
        command = "tc qdisc replace dev %s root handle 1:0 tbf rate %dkbit burst %dk limit %dkbit" % (
            self.veth_interface_list[1], self.bandwidth*8, self.bandwidth, self.bandwidth*8)
        
        exec_res = os.popen(command).read()
        command = "tc qdisc replace dev %s parent 1:0 handle 2:0 netem delay %dms loss %s" % (
            self.veth_interface_list[1], self.delay, self.loss)
        
        exec_res = os.popen(command).read()

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
    def close_veth(self):
        for veth_name in self.veth_interface_list:
            command = "ifconfig %s down" % veth_name
            exec_res = os.popen(command).read()

    def open_veth(self):
        for veth_name in self.veth_interface_list:
            command = "ifconfig %s up" % veth_name
            exec_res = os.popen(command).read()


"""
added by sqsq
used to print link events
"""
def print_link_event(network: Network, docker_client: DockerClient, lock, current_sim_time: float, event_type: str):
    connected_containers = docker_client.client.networks.get(network.br_id).containers
    if len(connected_containers) != 2:
        logger.error("network connecting %d caontainers" % len(connected_containers))
    src_container_name: str = connected_containers[0].name
    target_container_name: str = connected_containers[1].name
    with lock:
        logger.info(
            '{"sim_time": %.3f, "link": "%s <--> %s", "type": "%s"}'
            % (current_sim_time, src_container_name, target_container_name, event_type)
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
                    print_link_event(network, docker_client, lock, current_sim_time, "up")
                    network.is_down = False
                    sim_time_interval = random.expovariate(poisson_lambda)
                    network.down_moment = current_sim_time + sim_time_interval # set the next link down moment
                elif not network.is_down and current_sim_time > network.down_moment:
                    # link should turned to down
                    print_link_event(network, docker_client, lock, current_sim_time, "down")
                    network.is_down = True
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

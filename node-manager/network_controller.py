import time
import docker
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
        network_key = get_network_key(docker_client, container_id1, container_id2)
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
    return int(sqrt(dist_square) / LIGHT_SPEED)  # UNIT: ms
    # ZHF MODIFY
    # return 0


def get_network_key(docker_client: DockerClient, container_id1: str, container_id2: str) -> str:
    """
    modified by sqsq
    network_key is no longer based on container_id, but container_name
    to ensure correspondence during different runs
    """
    container_name1 = docker_client.client.containers.get(container_id1).name
    container_name2 = docker_client.client.containers.get(container_id2).name
    if container_name1 > container_name2:
        return container_name2 + container_name1
    else:
        return container_name1 + container_name2


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
    container_name_list: List[str] = [docker_client.client.containers.get(container_id).name
                                      for container_id in container_id_list]
    iflink_of_veth: Dict[str, str] = {}                     # veth_name -> iflink of veth
    # ifindex_of_container: Dict[str, Dict[str, str]] = {}    # container_name -> (eth_name -> ifindex of this eth)
    
    for veth_name in veth_list:                             # build iflink_of_veth
        iflink: str = os.popen(f"cat /sys/class/net/{veth_name}/iflink").read().strip()
        iflink_of_veth[veth_name] = iflink

    for veth_name, iflink in iflink_of_veth.items():        # for each veth, iterate through all containers to find an eth whose ifindex == iflink
        found = False
        while found == False:
            for container_name in container_name_list:
                output = docker_client.exec_cmd(container_name, ['sh', '-c', f"/get_ifindex.sh {iflink}"])
                # NOTE: may return not 0 because one of the containers does not have correspond eth
                if output[0] != 0 and len(output[1].decode().strip()) != 0:
                    logger.error(['sh', '-c', f"/get_ifindex.sh {iflink}"])
                    logger.error(f"container_name:{container_name}")
                    logger.error(output)
                    raise Exception('')
                elif output[0] == 0:
                    res: str = output[1].decode().strip()
                    if len(res) != 0:
                        eth_name = res.split('/')[-2]
                        veth_dict[container_name] = veth_name
                        eth_dict[container_name] = eth_name
                        found = True
                        break
            if found == False:
                logger.warning(f"not found correspond eth of {veth_name}(iflink={iflink}) in {container_name_list}")
                time.sleep(random.random() * 0.1)

                
    # for container_name in container_name_list:              # build ifindex_of_container
    #     ifindex_of_container[container_name] = {}
    #     ret = docker_client.exec_cmd(container_name, ['sh', '-c', 'ls /sys/class/net/'])    # using "sh -c" may prevent exec_cmd from retuning empty string
    #     if ret[0] != 0:
    #         logger.error(ret[1].decode().strip())
    #         raise Exception('get_inner_eth_dict failed')
    #     eth_names = ret[1].decode().strip().split('\n')
    #     flag = False
    #     if len(eth_names) == 0:
    #         flag = True
    #     else:
    #         for eth_name in eth_names:
    #             if len(eth_name) == 0:
    #                 flag = True
    #                 break
    #     while flag == True:
    #         flag = False
    #         time.sleep(random.random() * 0.1)
    #         logger.warning(f"container_name: {container_name}, eth_names:{eth_names}, len=0")
    #         ret = docker_client.exec_cmd(container_name, ['sh', '-c', 'ls /sys/class/net/'])
    #         if ret[0] != 0:
    #             logger.error(ret[1].decode().strip())
    #             raise Exception('get_inner_eth_dict failed')
    #         eth_names = ret[1].decode().strip().split('\n') 
    #         if len(eth_names) == 0:
    #             flag = True
    #         else:
    #             for eth_name in eth_names:
    #                 if len(eth_name) == 0:
    #                     flag = True
    #                     break
        
    #     for eth_name in eth_names:
    #         command = ['sh', '-c', f"cat /sys/class/net/{eth_name}/ifindex"]
    #         ret = docker_client.exec_cmd(container_name, command)
    #         if ret[0] != 0:
    #             logger.error(ret[1].decode().strip())
    #             logger.error(f'container_name: {container_name}    eth_names: {eth_names}')
    #             raise Exception('get_inner_eth_dict failed')
    #         else:
    #             ifindex = ret[1].decode().strip()
    #             while len(ifindex) == 0:
    #                 logger.warning(f"{container_name}.{eth_name}.ifindex = {ifindex}")
    #                 time.sleep(random.random() * 0.1)
    #                 ret = docker_client.exec_cmd(container_name, command)
    #                 if ret[0] != 0:
    #                     logger.error(ret[1].decode().strip())
    #                     logger.error(f'container_name: {container_name}    eth_names: {eth_names}')
    #                     raise Exception('get_inner_eth_dict failed')
    #             ifindex_of_container[container_name][eth_name] = ifindex

    # # for each container, iterate through all its eths
    # # and find a veth which iflink == ifindex of one of eths 
    # for container_name, ifindex_of_eth in ifindex_of_container.items():
    #     found = False
    #     for eth_name, ifindex in ifindex_of_eth.items():
    #         for veth_name, iflink in iflink_of_veth.items():
    #             if ifindex == iflink:
    #                 found = True
    #                 veth_dict[container_name] = veth_name
    #                 eth_dict[container_name] = eth_name
    #     if not found:
    #         logger.error(ifindex_of_container)
    #         logger.error(iflink_of_veth)
    #         logger.error(f'correspond veth of {container_name} not found')
    #         raise Exception('correspond veth not found')
    
    if len(set(veth_dict.values())) != 2 or len(veth_dict.keys()) != 2:
        # logger.error(ifindex_of_container)
        logger.error(iflink_of_veth)
        logger.error(f", veth_dict: {veth_dict}, eth_dict: {eth_dict}")
        raise Exception("bad ret_dict")

    # logger.info(f"veth_dict: {veth_dict}, eth_dict: {eth_dict}")

    return [veth_dict, eth_dict]


class Network:

    def __init__(self,
                 docker_client: DockerClient,
                 bridge_id: str,
                 container_id1: str,
                 container_id2: str,
                 delay: int,
                 band_width: int,
                 loss_percent: int,
                 queue_capacity: int):
        # 为保证network key的唯一性，设置map中key的字符串拼接顺序为小id在前,大id在后
        self.docker_client = docker_client
        self.br_id = bridge_id
        self.container_id1 = container_id1
        self.container_id2 = container_id2
        self.network_key = get_network_key(docker_client, container_id1, container_id2)
        self.br_interface_name = get_bridge_interface_name(bridge_id)
        self.veth_interface_list = get_vethes_of_bridge(self.br_interface_name)
        self.delay = delay              # unit: ms
        self.bandwidth = band_width     # unit: Mbps
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
        self.lock = Lock()

        self.init_info()


    def __hash__(self) -> int:
        return hash(self.network_key)

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
            command = ['sh', '-c', f'tc qdisc add dev {inner_eth_name} root netem delay {self.delay}ms rate {self.bandwidth}Mbit limit {self.queue_capacity}']
            ret = self.docker_client.exec_cmd(container_name, command)
            if ret[0] != 0:
                logger.error(ret[1].decode().strip())
                raise Exception('')

    def update_info(self):
        for container_name, inner_eth_name in self.inner_eth_dict.items():
            command = ['sh', '-c', f'tc qdisc replace dev {inner_eth_name} root netem delay {self.delay}ms rate {self.bandwidth} Mbitlimit {self.queue_capacity}']
            ret = self.docker_client.exec_cmd(container_name, command, stream=False, detach=True)

    def update_delay_param(self, set_time: int):
        self.delay = set_time
        if not self.is_down:
            self.update_info()

    def update_bandwidth_param(self, band_width: int):
        self.bandwidth = band_width
        if not self.is_down:
            self.update_info()

    def update_loss_param(self, loss_percent: int):
        self.loss = loss_percent
        if not self.is_down:
            self.update_info()

    
    def print_link_event(self, current_sim_time: float, type: str):
        container_name_list = sorted(list(self.inner_eth_dict.keys()))
        with open("link.log", "a") as f:
            print(
                '{"sim_time": %.3f, "link": "%s <--> %s", "type": "%s"}'
                % (current_sim_time, container_name_list[0], container_name_list[1], type),
                file=f,
                flush=True
            )    
        logger.info(
            '{"sim_time": %.3f, "link": "%s <--> %s", "type": "%s"}'
            % (current_sim_time, container_name_list[0], container_name_list[1], type)
        )


    # added by sqsq
    # set the next link down moment
    def set_down_moment(self, current_sim_time:float,  random_instance: random.Random, poisson_lambda: float):
        sim_time_interval = random_instance.expovariate(poisson_lambda)
        self.down_moment = current_sim_time + sim_time_interval 


    # added by sqsq
    def close_link(self, start_time: float):
        self.is_down = True

        for container_name, eth_name in self.inner_eth_dict.items():
            command = ['sh', '-c', f"ifconfig {eth_name} down"]
            self.docker_client.exec_cmd(container_name, command, stream=False, detach=True)
            # process = Process(target=self.docker_client.exec_cmd, args=(container_name, command))
            # process.start()

        current_sim_time = time.time() - start_time
        self.print_link_event(current_sim_time, "down")
        # process = Process(target=self.print_link_event, args=(current_sim_time, "down"))
        # process.start()


    def open_link(self, start_time: float, random_instance: random.Random, poisson_lambda: float):
        self.is_down = False
        self.update_info()
        current_sim_time = time.time() - start_time
        self.set_down_moment(current_sim_time, random_instance, poisson_lambda)

        for container_name, eth_name in self.inner_eth_dict.items():
            command = ['sh', '-c', f"ifconfig {eth_name} up"]
            self.docker_client.exec_cmd(container_name, command, stream=False, detach=True)
            # process = Process(target=self.docker_client.exec_cmd, args=(container_name, command))
            # process.start()

        current_sim_time = time.time() - start_time
        self.print_link_event(current_sim_time, "up")
        # process = Process(target=self.print_link_event, args=(current_sim_time, "up"))
        # process.start()


def generate_link_failure(docker_client: DockerClient, link_failure_rate: float, seed: int = None):
    """
    added by sqsq
    for link failure generating
    @parameter seed: use this seed to generate random seeds of each network in random_instance_dict
    """
    if abs(link_failure_rate - 0) < 1e-6:
        return
    
    random_instance_dict: Dict[Network, random.Random] = {}
    if seed is not None:
        random.seed(seed)
    sorted_keys = sorted(network_dict.keys())
    for key in sorted_keys:   
        # generate random instance for each network
        # NOTE: sort to ensure each network's random_instance is the same during different runs
        network = network_dict[key]
        random_instance_seed = random.randint(0, 100000)
        random_instance_dict[network] = random.Random(random_instance_seed)
        # with open("seed.txt", "a") as f:
        #     print(f"network key:{network.network_key}, seed:{random_instance_seed}/{random_instance_dict[network].getstate()[1][0]}", file=f)    
    if seed is not None:
        random.seed(None)

    poisson_lambda = link_failure_rate / (LINK_FAILURE_DURATION * (1 - link_failure_rate))
    start_time = time.time()

    for network in network_dict.values():   # generate first down moment
        random_instance = random_instance_dict[network]
        network.set_down_moment(0.0, random_instance, poisson_lambda)
    
    flag = False
    while True:
         if (flag):
             break
         for network in network_dict.values():

            current_sim_time = time.time() - start_time
            # logger.debug(f"current_simtime: {current_sim_time}")

            if current_sim_time <= SIMULATION_DURATION:
                if network.is_down and current_sim_time <= network.down_moment + LINK_FAILURE_DURATION:
                    # link is in down state
                    continue
                elif network.is_down and current_sim_time > network.down_moment + LINK_FAILURE_DURATION:
                    # link should recover
                    # process_open_link = Process(target=network.open_link, args=(start_time, random_instance, poisson_lambda))
                    network.open_link(start_time, random_instance_dict[network], poisson_lambda)
                    # process_open_link.start()
                elif not network.is_down and current_sim_time > network.down_moment:
                    # link should turned to down
                    # process_close_link = Process(target=network.close_link, args=(start_time, ))
                    network.close_link(start_time)
                    # process_close_link.start()
                else:
                    continue

                current_sim_time = time.time() - start_time
                if current_sim_time >= SIMULATION_DURATION:
                    break
            else:   # sim time exceeded, loop should stop
                flag = True  


def update_network_delay(docker_client: DockerClient, position_data: dict, topo: dict):
    for start_node_id in topo.keys():
        conn_array = topo[start_node_id]
        for target_node_id in conn_array:
            start_node_id_str = satellite_id_tuple_to_str(start_node_id)
            target_node_id_str = satellite_id_tuple_to_str(target_node_id)
            delay = get_laser_delay_ms(position_data[start_node_id_str],position_data[target_node_id_str])
            start_container_id = satellite_map[start_node_id].container_id
            target_container_id = satellite_map[target_node_id].container_id
            net_object = network_dict[get_network_key(docker_client, start_container_id,target_container_id)]
            net_object.update_delay_param(delay)


if __name__ == '__main__':
    print(generate_submission_list_for_network_object_creation([1, 2, 3, 4, 5], 1))

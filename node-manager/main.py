import multiprocessing
import multiprocessing.managers
import subprocess
import os.path
import time
import typing
import sys
import socket
import random
from ctypes import c_bool
from multiprocessing import Process, Manager, Queue
from loguru import logger
from config_monitor import init_monitor, connect_monitor, set_monitor
from const_var import *
from constellation_creator import constellation_creator
from data_updater import DataUpdater
from docker_client import DockerClient
from position_broadcaster import position_broadcaster
from satellite_config import Config
from tle_generator import generate_tle
from delete_containers_and_networks import delete_containers_with_multiple_processes, \
    delete_networks_with_multiple_processes
from network_controller import generate_link_failure, update_network_delay
from global_var import connect_order_map, satellite_map, reinit_global_var
from ground_station import create_station_from_json
from tools import *
from transmission_test import start_transmission_test, start_packet_capture, get_ip_of_node_id


def delete_constellation(docker_client: DockerClient):
    delete_containers_with_multiple_processes(docker_client, SUBMISSION_SIZE_FOR_DELETE_CONTAINER)
    delete_networks_with_multiple_processes(docker_client, SUBMISSION_SIZE_FOR_DELETE_NETWORK)
    os.system("./stop_and_kill_constellation.sh")


def logger_file_filter(record):
    if "now drop rate" in record["message"]:
        return True
    return False


def install_kernel_module(command: str) -> None:
    try:
        output = subprocess.check_output(command, 
                                        shell=True, 
                                        stderr=subprocess.STDOUT, 
                                        universal_newlines=True)
    except subprocess.CalledProcessError as e:
        logger.error(e.output)
        raise Exception('')
    logger.success(output)


def uninstall_kernel_modules() -> None:
    os.system("./sqsq-kernel-modules/uninstall_modules.sh")


def start_frr(docker_client: DockerClient) -> None:
    process_list: typing.List[Process] = []
    logger.info('copying frr.conf to containers')
    for id in satellite_map.keys():
        container_name = satellite_id_tuple_to_str(id)
        process_copy = Process(target=docker_client.copy_to_container, 
                               args=(container_name, 
                                     f'../configuration/frr/{container_name}.conf', 
                                     f'/etc/frr/frr.conf'))
        process_list.append(process_copy)
    for process_copy in process_list:
        process_copy.start()
    for process_copy in process_list:
        process_copy.join()

    process_list.clear()
    logger.info('starting frr in containers')
    for id in satellite_map.keys():
        process_start_frr = Process(target=docker_client.exec_cmd, 
                                    args=(satellite_id_tuple_to_str(id), 
                                          './usr/lib/frr/frrinit.sh start'))
        process_list.append(process_start_frr)
    for process_start_frr in process_list:
        process_start_frr.start()
    for process_start_frr in process_list:
        process_start_frr.join()
    logger.info('waiting for frr init')
    time.sleep(WARMUP_PERIOD)


def start_load_awareness(docker_client: DockerClient, lofi_delta: float):
    process_list: typing.List[Process] = []    
    cmd = f"/load_wawreness/load_awareness {lofi_delta} {QUEUE_CAPACITY} {NETWORK_BANDWIDTH*1000000} {1024 * 8} " \
            + f"{NETWORK_DELAY} {NETWORK_DELAY} {NETWORK_DELAY} {NETWORK_DELAY}"
    if enable_load_awareness:
        for id in satellite_map.keys():
            process_start_load_wawreness = Process(target=docker_client.exec_cmd, 
                                                   args=(satellite_id_tuple_to_str(id), cmd, False, True))
            process_list.append(process_start_load_wawreness)
        for process_start_load_wawreness in process_list:
            process_start_load_wawreness.start()
        for process_start_load_wawreness in process_list:
            process_start_load_wawreness.join()


def set_satellite_id_in_kernel(docker_client: DockerClient):
    logger.info('configuring satellite id in kernel net ns')
    for id in satellite_map.keys():
        satellite_name = satellite_id_tuple_to_str(id)
        satellite_id = socket.htonl(ip_str_to_int(f"0.0.{id[0]}.{id[1]}"))
        logger.info(f"configuring kernel net id {satellite_id}(0.0.{id[0]}.{id[1]}) to {satellite_name}: "
              f"/set-satellite-id/set_satellite_id {satellite_id}")
        ret = docker_client.exec_cmd(satellite_name, f"/set-satellite-id/set_satellite_id {satellite_id}")
        logger.info(ret[1].decode().strip())
        while ret[0] != 0:
            logger.warning(ret[1].decode().strip())
            time.sleep(random.random())
            ret = docker_client.exec_cmd(satellite_name, f"/set-satellite-id/set_satellite_id {satellite_id}")
            logger.info(ret[1].decode().strip())


def start_simulation(docker_client: DockerClient, link_failure_rate: float, send_interval: float, test: int, random_seed: int):
    process_list = []
    simulation_start_time = time.time()
    generate_link_failure_process = Process(target=generate_link_failure, 
                                            args=(docker_client, link_failure_rate, RECEIVER_NODE_ID, simulation_start_time, random_seed))
    # generate_link_failure_process = Process(target=generate_link_failure, 
    #                                         args=(docker_client, link_failure_rate, RECEIVER_NODE_ID, simulation_start_time, test))
    generate_link_failure_process.start()	# start link failure generation

    time.sleep(10)							# start udp transmitting
    manager = Manager()
    shared_result_list: multiprocessing.managers.ListProxy[typing.Dict[str, str]] = manager.list() # shared_result_list: list[dict]
    start_transmission_test_process = Process(target=start_transmission_test, 
                                                args=(docker_client, send_interval, shared_result_list, simulation_start_time))
    process_list.append(start_transmission_test_process)

    logger.info("transmission starting...")
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    generate_link_failure_process.terminate()

    logger.info(shared_result_list)
    
    drop_rate = shared_result_list[0]['drop rate'].strip()
    delay = shared_result_list[0]['delay'].strip()
    ttl_rate = shared_result_list[1]['ttl_drop_ratio']
    no_entry_rate = shared_result_list[2]['no_entry_ratio']
    throughput = shared_result_list[3]['throughput']
    control_overhead = shared_result_list[3]['control overhead']

    with open('./result_tmp.csv', 'a') as f:
        print(f"{lofi_n},{enable_load_awareness},{lofi_delta},"
                f"{link_failure_rate},{random_seed},{test},"
                f"{drop_rate},{delay},{throughput},{control_overhead},"
                f"{ttl_rate},{no_entry_rate}", file=f)

    # copy network events from container to host
    process_list.clear()
    for id in satellite_map.keys():
        container_name = satellite_id_tuple_to_str(id)
        process_copy = Process(target=docker_client.copy_from_container, 
                                args=(container_name, 
                                        f'/var/log/network_events.log', 
                                        f'../container-events/{container_name}_network_events.log'))
        process_list.append(process_copy)
    for process_copy in process_list:
        process_copy.start()
    for process_copy in process_list:
        process_copy.join()

def run(enable_load_awareness: bool, lofi_delta: float, lofi_n: int, 
        link_failure_rate: float, send_interval: float, test: int, random_seed: int, dry_run = False):
    reinit_global_var()
    # the share bool value
    stop_process_state = multiprocessing.Value(c_bool, False)
    # read config.ini file
    # ---------------------------------
    file_path = os.path.abspath('.') + '/config.ini'
    config = Config(file_path)
    host_ip = config.DockerHostIP
    ground_image_name = config.GroundImageName
    udp_port = config.UDPPort
    monitor_image_name = config.MonitorImageName
    # ---------------------------------

    init_start_time = time.time()

    # ---------------------------------
    # check for ospf
    if lofi_n == -1:
        image_name = "ospf:latest"
        enable_load_awareness = False
    elif lofi_n == -2:
        image_name = "elb:latest"
        enable_load_awareness = False
    # ---------------------------------

    # create position updater
    # ----------------------------------------------------------
    updater = DataUpdater("<broadcast>", host_ip, int(udp_port))
    # ----------------------------------------------------------

    logger.info(f"host ip:{host_ip}, udp port:{udp_port}")

    # create docker client
    # ----------------------------------------------------------
    docker_client = DockerClient(image_name, host_ip, ground_image_name)
    # ----------------------------------------------------------

    # create monitor
    # ----------------------------------------------------------
    successful_init = init_monitor(monitor_image_name, docker_client, udp_port)

    # ----------------------------------------------------------

    # start send monitor data
    connect_monitor()
    
    # ---------------------------------
    # install kernel modules, added by sqsq
    uninstall_kernel_modules()
    install_kernel_module(f"./sqsq-kernel-modules/install_satellite_id.sh")
    if enable_load_awareness:
        install_kernel_module("./sqsq-kernel-modules/install_load_awareness.sh")
    # ---------------------------------

    # generate satellite infos
    # ----------------------------------------------------------------
    orbit_num = ORBIT_NUM
    satellites_per_orbit = SAT_PER_ORBIT
    satellite_infos, connections = generate_tle(orbit_num, satellites_per_orbit, 0, 0, 0.01, 0.08)
    # logger.info(satellite_infos)
    # logger.info(connections)
    satellite_num = len(satellite_infos)
    # ----------------------------------------------------------------

    # generate constellation
    # ----------------------------------------------------------------------------------------------------
    position_datas, monitor_payloads = constellation_creator(docker_client, satellite_infos, connections, host_ip,
                                                             udp_port, successful_init, lofi_n=lofi_n)
    # ----------------------------------------------------------------------------------------------------
    # ground_stations = create_station_from_json(docker_client, config.GroundConfigPath)
    ground_stations = {}

    # -------------------------------------------------------------------

    # added by sqsq
    # set the initial position
    # -------------------------------------------------------------------
    for node_id in sorted(list(satellite_map.keys())):
        satellite_node = satellite_map[node_id]
        node_id_str = satellite_id_tuple_to_str(node_id)
        position_datas[node_id_str][LATITUDE_KEY], \
        position_datas[node_id_str][LONGITUDE_KEY], \
        position_datas[node_id_str][HEIGHT_KEY] = satellite_node.get_next_position(TIME_BASE)
        # logger.info(f"{node_id_str}: {position_datas[node_id_str]}")
    update_network_delay(docker_client, position_datas, connect_order_map)
    # -------------------------------------------------------------------

    # -------------------------------------------------------------------
    init_end_time = time.time()
    logger.info(f'constellation init time: {init_end_time - init_start_time: .3f}s')
    # -------------------------------------------------------------------

    # -------------------------------
    # install kernel modules part 2
    if lofi_n != -1:
        install_kernel_module("./sqsq-kernel-modules/install_multipath.sh")

    receiver_ip_str = get_ip_of_node_id(docker_client, RECEIVER_NODE_ID)
    receiver_ip_int = ip_str_to_int(receiver_ip_str)
    install_kernel_module(f"./sqsq-kernel-modules/install_packet_drop.sh {receiver_ip_int}")
    # ---------------------------------

    # -------------------------------------------------------------------
    # start frr    added by sqsq
    start_frr(docker_client)
    # -------------------------------------------------------------------
        
    # -------------------------------------------------------------------
    # start load awareness, added by sqsq
    start_load_awareness(docker_client, lofi_delta)
    # -------------------------------------------------------------------
    
    os.system("dmesg -c > /dev/null")

    # set satellite id in kernel
    # -------------------------------------------------------------------
    set_satellite_id_in_kernel(docker_client)
    # -------------------------------------------------------------------
    
    # set monitor
    # ----------------------------------------------------------
    set_monitor_process = Process(target=set_monitor, 
                                  args=(monitor_payloads, ground_stations, stop_process_state, 20))
    set_monitor_process.start()
    # ----------------------------------------------------------

    # start position broadcaster and update network delay
    # comment by sqsq
    # ----------------------------------------------------------
    # update_position_process = Process(target=position_broadcaster, args=(docker_client, 
    #                                                                      stop_process_state,
    #                                                                      satellite_num,
    #                                                                      position_datas,
    #                                                                      updater,
    #                                                                      BROADCAST_SEND_INTERVAL,
    #                                                                      connect_order_map))
    # update_position_process.start()
    # ----------------------------------------------------------

    # start link failure generation and UDP send & recv
    # added by sqsq
    # ----------------------------------------------------------
    logger.info('test starting...')

    if not dry_run:
        start_simulation(docker_client, link_failure_rate, send_interval, test, random_seed)
    else:
        while True:
            pass
    # ----------------------------------------------------------
        
    # ----------------------------------------------------------
    # clear after one run
    set_monitor_process.kill()
    # update_position_process.kill()
    delete_constellation(docker_client)

    logger.success('finished 1 test')

    os.system("clear")
    uninstall_kernel_modules()
    # ----------------------------------------------------------


if __name__ == "__main__":
    # check sudo permission
    sudo_uid = os.environ.get('SUDO_UID')
    if sudo_uid is None:
        raise Exception("\nneed to have sudo permission.\n try sudo python3 main.py")
    
    # record long-term result to file
    logger.add("long_term_result.log", filter=logger_file_filter)

    if DRY_RUN == True:
        logger.warning('DRY_RUN is set to True, enter y to continue')
        text = input()
        if text != "y":
            logger.info('stop running')
            sys.exit()
    
    os.system("./stop_and_kill_constellation.sh")

    log_file_list = ["eth_dict.log", "link.log", "long_term_result.log", "kernel.log", "nettrace.log"]
    for log_file in log_file_list:
        with open(log_file, "w") as f:
            print("", flush=True, file=f)

    # lofi_n = -1 means using ospf
    # lofi_n = -2 means using elb
    enable_load_awareness = False
    lofi_delta = 0.05
    link_failure_rate_list = [0.05]
    # lofi_n_list = [-1]
    # test_nums = [1]
    # random_seeds = [42]
    lofi_n_list = [4, 5, 6, -1]
    test_nums = [10, 10, 10, 10]
    random_seeds = [42 + i for i in range(RANDOM_SEED_NUM)]

    if (len(lofi_n_list) != len(test_nums)):
        raise Exception('lofi_n_list and test_nums not correspond')

    if not os.path.exists('./result_tmp.csv') and not DRY_RUN:
        with open('./result_tmp.csv', 'w') as f:
            print('lofi_n,load_awareness,lofi_delta,'
                  'link_failure_rate,random_seed,test,'
                  'drop_rate,delay,throughput,control_overhead,'
                  'ttl_rate,no_entry_rate', file=f)
        os.system("chmod 777 ./result_tmp.csv")

    for link_failure_rate in link_failure_rate_list:
        for i, lofi_n in enumerate(lofi_n_list):
            if RECORD_LONG_TERM_RESULT:
                with open('./long_term_result.log', 'a') as f:
                    print(f"failure: {link_failure_rate}, n: {lofi_n}", file=f, flush=True)
            for random_seed in random_seeds:
                for test in range(1, test_nums[i] + 1):
                    run(enable_load_awareness, lofi_delta, lofi_n, 
                        link_failure_rate, UDP_SEND_INTERVAL, test, random_seed, DRY_RUN)

    

    
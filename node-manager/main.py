import multiprocessing
import subprocess
import os.path
import time
import typing
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


def run(enable_load_awareness: bool, lofi_delta: float, lofi_n: int, 
        link_failure_rate: float, send_interval: float, test: int, dry_run = False):
    reinit_global_var()
    # the share bool value
    stop_process_state = multiprocessing.Value(c_bool, False)
    # read config.ini file
    # ---------------------------------
    file_path = os.path.abspath('.') + '/config.ini'
    config = Config(file_path)
    host_ip = config.DockerHostIP
    image_name = config.DockerImageName
    ground_image_name = config.GroundImageName
    udp_port = config.UDPPort
    monitor_image_name = config.MonitorImageName
    # ---------------------------------

    init_start_time = time.time()

    # ---------------------------------
    # check for ospf
    if image_name == "ospf:latest":
        lofi_n = -1
        enable_load_awareness = False
    elif lofi_n == -1:
        image_name = "ospf:latest"
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
        position_datas[node_id_str][LATITUDE_KEY], position_datas[node_id_str][LONGITUDE_KEY], position_datas[node_id_str][HEIGHT_KEY] = satellite_node.get_next_position(TIME_BASE)
        # logger.info(f"{node_id_str}: {position_datas[node_id_str]}")
    update_network_delay(docker_client, position_datas, connect_order_map)
    # -------------------------------------------------------------------

    # -------------------------------------------------------------------
    init_end_time = time.time()
    logger.info(f'constellation init time: {init_end_time - init_start_time: .3f}s')
    # -------------------------------------------------------------------

    # start frr    added by sqsq
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
    # -------------------------------------------------------------------
        
    # ---------------------------------
    # start kernel modules, added by sqsq
    os.system("./sqsq-kernel-modules/uninstall_modules.sh")
    module_script_list = []

    receiver_ip_str = get_ip_of_node_id(docker_client, RECEIVER_NODE_ID)
    receiver_ip_int = ip_str_to_int(receiver_ip_str)

    if lofi_n != -1:
        module_script_list.append("./sqsq-kernel-modules/install_multipath.sh")
    if enable_load_awareness:
        module_script_list.append("./sqsq-kernel-modules/install_load_awareness.sh")
    module_script_list.append(f"./sqsq-kernel-modules/install_packet_drop.sh {receiver_ip_int}")
    for module_path in module_script_list:
        try:
            output = subprocess.check_output(module_path, 
                                            shell=True, 
                                            stderr=subprocess.STDOUT, 
                                            universal_newlines=True)
        except subprocess.CalledProcessError as e:
            logger.error(e.output)
            raise Exception('')
        logger.success(output)    
    # ---------------------------------
        
    # -------------------------------------------------------------------
    # start load awareness, added by sqsq
    process_list.clear()    
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
    logger.info('waiting for init...')
    time.sleep(WARMUP_PERIOD)
    process_list.clear()
    logger.info('test starting...')

    if not dry_run:
        generate_link_failure_process = Process(target=generate_link_failure, 
                                                args=(docker_client, link_failure_rate, RECEIVER_NODE_ID, 42))
        process_list.append(generate_link_failure_process)

        manager = Manager()
        shared_result_list = manager.list() # shared_result_list: list[dict]
        start_transmission_test_process = Process(target=start_transmission_test, 
                                                  args=(docker_client, send_interval, shared_result_list))
        process_list.append(start_transmission_test_process)

        queue = Queue() # queue of dict
        start_packet_capture_process = Process(target=start_packet_capture, args=(queue, ))
        process_list.append(start_packet_capture_process)

        logger.info("transmission starting...")
        for process_copy in process_list:
            process_copy.start()
        for process_copy in process_list:
            process_copy.join()

        logger.info(shared_result_list)
        
        drop_rate = shared_result_list[0]['drop rate']
        delay = shared_result_list[0]['delay']
        ttl_rate = shared_result_list[1]['ttl_drop_ratio']
        no_entry_rate = shared_result_list[2]['no_entry_ratio']

        queue_element = queue.get()
        throughput = queue_element['throughput']
        control_overhead = queue_element['control overhead']

        with open('./result_tmp.csv', 'a') as f:
            print(f"{lofi_n},{enable_load_awareness},{lofi_delta},"
                  f"{link_failure_rate},{test},"
                  f"{drop_rate},{delay},{throughput},{control_overhead},"
                  f"{ttl_rate},{no_entry_rate}", file=f)

        # copy etwork events from container to host
        process_list = []
        for id in satellite_map.keys():
            container_name = satellite_id_tuple_to_str(id)
            process_copy = Process(target=docker_client.copy_from_container, 
                                   args=(container_name, 
                                         f'/var/log/network_events.log', 
                                         f'../container-events/{container_name}_network_events.log'))
            # process_copy = Process(target=docker_client.copy_from_container(), 
            #                     args=(container_name, 
            #                           f'/var/log/rtmon.log', 
            #                           f'../container_events/{container_name}_rtmon.log'))
            process_list.append(process_copy)
        for process_copy in process_list:
            process_copy.start()
        for process_copy in process_list:
            process_copy.join()

        set_monitor_process.kill()
        # update_position_process.kill()
        delete_constellation(docker_client)
        os.system("clear")
    else:
        while True:
            pass
    # ----------------------------------------------------------
        
    # ----------------------------------------------------------
    # uninstall kernel modules
    os.system("./sqsq-kernel-modules/uninstall_modules.sh")
    # ----------------------------------------------------------


if __name__ == "__main__":
    # check sudo permission
    sudo_uid = os.environ.get('SUDO_UID')
    if sudo_uid is None:
        raise Exception("\nneed to have sudo permission.\n try sudo python3 main.py")
    
    os.system("./stop_and_kill_constellation.sh")

    with open("eth_dict.log", "w") as f:
        print("", flush=True, file=f)
    with open("link.log", "w") as f:
        print("", flush=True, file=f)

    enable_load_awareness = False
    lofi_delta = 0.05
    # link_failure_rate_list = [0, 0.01, 0.02, 0.03, 0.04, 0.05]
    lofi_n_list = [0]
    link_failure_rate_list = [0.05]
    # lofi_n_list = [-1, 2, 4]
    test_nums = [5]

    if (len(lofi_n_list) != len(test_nums)):
        raise Exception('lofi_n_list and test_nums not correspond')

    if not os.path.exists('./result_tmp.csv') and not DRY_RUN:
        with open('./result_tmp.csv', 'w') as f:
            print('lofi_n,load_awareness,lofi_delta,'
                  'link_failure_rate,test,'
                  'drop_rate,delay,throughput,control_overhead,'
                  'ttl_rate,no_entry_rate', file=f)
        os.system("chmod 777 ./result_tmp.csv")

    for link_failure_rate in link_failure_rate_list:
        for i, lofi_n in enumerate(lofi_n_list):
            for test in range(1, test_nums[i] + 1):
                run(enable_load_awareness, lofi_delta, lofi_n, 
                    link_failure_rate, UDP_SEND_INTERVAL, test, DRY_RUN)

    

    
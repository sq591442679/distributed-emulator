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
from network_controller import generate_link_failure
from global_var import connect_order_map, satellite_map, reinit_global_var
from ground_station import create_station_from_json
from tools import *
from transmission_test import start_transmission_test, start_packet_capture


def run(lofi_n: int, link_failure_rate: float, send_interval: float, test: int, dry_run = False):
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

    #-------------------------------------------------------------------
    # start frr    added by sqsq
    process_list: typing.List[Process] = []
    logger.info('copying frr.conf to containers')
    for id in satellite_map.keys():
        id_str = satellite_id_tuple_to_str(id)
        process_copy = Process(target=docker_client.copy_to_container, args=(id_str, f'../configuration/frr/{id_str}.conf', f'/etc/frr/frr.conf'))
        process_list.append(process_copy)
    for process_copy in process_list:
        process_copy.start()
    for process_copy in process_list:
        process_copy.join()

    process_list.clear()
    logger.info('starting frr in containers')
    for id in satellite_map.keys():
        process_start_frr = Process(target=docker_client.exec_cmd, args=(satellite_id_tuple_to_str(id), './usr/lib/frr/frrinit.sh start'))
        process_list.append(process_start_frr)
    for process_start_frr in process_list:
        process_start_frr.start()
    for process_start_frr in process_list:
        process_start_frr.join()
    #-------------------------------------------------------------------
    
    # set monitor
    # ----------------------------------------------------------
    # set_monitor_process = Process(target=set_monitor, args=(monitor_payloads, ground_stations, stop_process_state, 20))
    # set_monitor_process.start()
    # ----------------------------------------------------------

    # start position broadcaster and update network delay
    # comment by sqsq
    # ----------------------------------------------------------
    update_position_process = Process(target=position_broadcaster, args=(docker_client, 
                                                                         stop_process_state,
                                                                         satellite_num,
                                                                         position_datas,
                                                                         updater,
                                                                         BROADCAST_SEND_INTERVAL,
                                                                         connect_order_map))
    update_position_process.start()
    # ----------------------------------------------------------

    # start link failure generation and UDP send & recv
    # added by sqsq
    # ----------------------------------------------------------
    time.sleep(10)
    logger.info("transmission starting...")
    process_list.clear()

    generate_link_failure_process = Process(target=generate_link_failure, args=(docker_client, link_failure_rate, 42))
    process_list.append(generate_link_failure_process)

    manager = Manager()
    shared_result_list = manager.list() # shared_result_list: list[dict]
    start_transmission_test_process = Process(target=start_transmission_test, args=(docker_client, send_interval, shared_result_list))
    process_list.append(start_transmission_test_process)

    queue = Queue() # queue of dict
    start_packet_capture_process = Process(target=start_packet_capture, args=(queue, ))
    process_list.append(start_packet_capture_process)

    for process_copy in process_list:
        process_copy.start()
    for process_copy in process_list:
        process_copy.join()
    
    drop_rate = shared_result_list[0]['drop rate']
    delay = shared_result_list[0]['delay']

    queue_element = queue.get()
    throughput = queue_element['throughput']
    control_overhead = queue_element['control overhead']

    if not dry_run:
        with open('./result.csv', 'a') as f:
            print(f"{lofi_n},{link_failure_rate},{test},{drop_rate},{delay},{throughput},{control_overhead}", file=f)
    else:
        logger.info(f"n:{lofi_n}, fr:{link_failure_rate}, test:{test},\n"
                    f"drop rate:{drop_rate}, delay:{delay},\n"
                    f"throughput:{throughput}, overhead:{control_overhead}")

    # set_monitor_process.kill()
    update_position_process.kill()
    os.system("./stop_and_kill_constellation.sh")
    os.system("clear")
    # ----------------------------------------------------------


if __name__ == "__main__":
    # check sudo permission
    sudo_uid = os.environ.get('SUDO_UID')
    if sudo_uid is None:
        raise Exception("\nneed to have sudo permission.\n try sudo python3 main.py")
    
    os.system("./stop_and_kill_constellation.sh")

    # start kernel modules, added by sqsq
    os.system("./sqsq-kernel-modules/uninstall_modules.sh")
    try:
        output = subprocess.check_output("./sqsq-kernel-modules/install_multipath.sh", 
                                         shell=True, 
                                         stderr=subprocess.STDOUT, 
                                         universal_newlines=True)
    except subprocess.CalledProcessError as e:
        logger.error(e.output)
        raise Exception('')
    logger.success(output)    
    
    dry_run = False
    # link_failure_rate_list = [0, 0.01, 0.02, 0.03, 0.04]
    # lofi_n_list = [0, 1, 2, 3, 4]
    link_failure_rate_list = [0.01, 0.05]
    lofi_n_list = [1]

    if not os.path.exists('./result.csv') and not dry_run:
        with open('./result.csv', 'w') as f:
            print('lofi_n,link_failure_rate,test,drop_rate,delay,throughput,control_overhead', file=f)
        os.system("chmod 777 ./result.csv")

    for link_failure_rate in link_failure_rate_list:
        for lofi_n in lofi_n_list:
            for test in range(1, TEST_NUM + 1):
                run(lofi_n, link_failure_rate, 0.1, test, dry_run)

    os.system("./sqsq-kernel-modules/uninstall_modules.sh")

    
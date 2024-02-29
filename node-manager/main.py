import multiprocessing
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
from network_controller import update_network_delay_with_multi_process, generate_link_failure
from global_var import connect_order_map, satellite_map, reinit_global_var
from ground_station import create_station_from_json
from tools import *
from transmission_test import start_transmission_test, start_packet_capture


if __name__ == "__main__":
    # check sudo permission
    sudo_uid = os.environ.get('SUDO_UID')
    if sudo_uid is None:
        raise Exception("\nneed to have sudo permission.\n try sudo python3 main.py")

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

    print(host_ip, int(udp_port))

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
    logger.info(connections)
    satellite_num = len(satellite_infos)
    # ----------------------------------------------------------------

    # generate constellation
    # ----------------------------------------------------------------------------------------------------
    position_datas, monitor_payloads = constellation_creator(docker_client, satellite_infos, connections, host_ip,
                                                             udp_port, successful_init, lofi_n=2)
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
    set_monitor_process = Process(target=set_monitor, args=(monitor_payloads, ground_stations, stop_process_state, 20))
    set_monitor_process.start()
    # ----------------------------------------------------------

    # start position broadcaster and update network delay
    # ----------------------------------------------------------
    update_position_process = Process(target=position_broadcaster, args=(stop_process_state,
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

    generate_link_failure_process = Process(target=generate_link_failure, args=(docker_client, 0.1))
    process_list.append(generate_link_failure_process)

    manager = Manager()
    shared_result_list = manager.list()
    start_transmission_test_process = Process(target=start_transmission_test, args=(docker_client, 0.1, shared_result_list))
    process_list.append(start_transmission_test_process)

    queue = Queue()
    start_packet_capture_process = Process(target=start_packet_capture, args=(queue, ))
    process_list.append(start_packet_capture_process)

    for process_copy in process_list:
        process_copy.start()
    for process_copy in process_list:
        process_copy.join()
    
    logger.success(shared_result_list[0])
    logger.success(queue.get())

    set_monitor_process.kill()
    update_position_process.kill()
    # os.system("./stop_and_kill_constellation.sh")
    # ----------------------------------------------------------

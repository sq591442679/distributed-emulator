import json
from datetime import datetime, timedelta
import multiprocessing as mp
from satellite_node import worker,satellites
from const_var import *
from global_var import *
from loguru import logger
import time
from multiprocessing import Pipe
from ground_station import ground_select,ground_stations
from network_controller import update_network_delay
from tools import *


def generate_submission_list_for_position_broadcaster(satellite_num, cpu_count):
    if cpu_count < satellite_num:
        # each cpu handle several satellites
        submission_size = (satellite_num // cpu_count) + 1
        submission_list = []
        # [0-2] [3-5] [6-8] [9-9]
        for i in range(0, satellite_num, submission_size):
            if i + submission_size - 1 > satellite_num:
                submission_list.append((i, satellite_num - 1))
            else:
                submission_list.append((i, i + submission_size - 1))
    else:
        # each satellite is handled by one cpu
        submission_list = [(i, i) for i in range(satellite_num)]
    # logger.info(submission_list)
    return submission_list


def position_broadcaster(docker_client, stop_process_state, satellite_num, position_datas, updater, sending_interval,topo):
    # create a config command and send out the command
    # ------------------------------------------------
    config_message = {"config": "set the source routing table"}
    config_str = json.dumps(config_message)
    updater.broadcast_info(config_str)
    # ------------------------------------------------

    # ------------------------------------------------
    # record sim time, added by sqsq
    start_time = datetime.now()

    # update position
    # ------------------------------------------------
    # 打印cpu的数量
    cpu_count = min(mp.cpu_count(), satellite_num)
    # logger.info(f"cpu_count: {cpu_count}")
    # 共享数组
    res = mp.Array('f', range(3 * satellite_num), lock=False)
    first_time = True
    # 创建进程
    # 创建子任务
    submission_list = generate_submission_list_for_position_broadcaster(satellite_num, cpu_count)
    while True:
        if stop_process_state.value:
            break
        current_count = 0
        multiple_processes = []
        # 创建管道
        rcv_pipe, send_pipe = Pipe()
        for i in range(len(submission_list)):
            now_time = datetime.now()
            now_sim_time = now_time - start_time + TIME_BASE

            # with open("sim_time.log", "a") as f:
            #     print(f"sim time: {now_sim_time}", file=f, flush=True)

            p = mp.Process(target=worker, args=(now_sim_time,
                                                submission_list[i][0],
                                                submission_list[i][1],
                                                res,
                                                send_pipe))
            multiple_processes.append(p)
            p.start()
        while True:
            # rcv_int = rcv_pipe.recv()
            # current_count += rcv_int
            # # print(f"current_count: {current_count}")
            # if current_count < satellite_num:
            #     continue
            # else:
                for i, satellite_node in enumerate(satellites):
                    node_id = satellite_node.node_id
                    index_base = 3 * i
                    node_id_str = satellite_id_tuple_to_str(node_id)
                    position_datas[node_id_str][LATITUDE_KEY] = res[index_base]
                    position_datas[node_id_str][LONGITUDE_KEY] = res[index_base + 1]
                    position_datas[node_id_str][HEIGHT_KEY] = res[index_base + 2]
                update_network_delay(position_datas, topo)
                ground_connections = ground_select(satellites, position_datas, ground_stations)
                broadcast_data = {
                    "position_datas": position_datas,
                    "ground_connections": ground_connections
                }
                data_str = json.dumps(broadcast_data)
                updater.broadcast_info(data_str)
                
                for p in multiple_processes:
                    p.kill()
                send_pipe.close()
                rcv_pipe.close()
                break
        
        with open("satellite_position.log", "a") as f:
            logger_data = {
                (j, 0): [now_sim_time.strftime("%Y-%m-%d %H:%M:%S.%f"), position_datas[satellite_id_tuple_to_str((j, 0))]] for j in range(ORBIT_NUM)
            }
            print(logger_data, file=f, flush=True)

        time.sleep(sending_interval)
    logger.success("position broadcaster process finished")


if __name__ == "__main__":
    print(generate_submission_list_for_position_broadcaster(320, 64))

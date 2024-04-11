import socket
import sys
import pickle
import time
from typing import List, Dict
import json

if __name__ == '__main__':
    local_ip = str(sys.argv[1])
    local_port = int(sys.argv[2])
    total_send_duration = float(sys.argv[3])
    total_receive_duration = float(sys.argv[4])
    expected_receive_cnt = int(sys.argv[5])

    receive_cnt = 0
    avg_delay = 0

    result_dict_list:List[Dict[str, str]] = []

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((local_ip, local_port))
    udp_socket.settimeout(1.0)

    # print('receiving UDP on ' + local_ip, flush=True)

    start_time = time.time()
    last_time = start_time

    while True:
        try:
            current_time = time.time()
            if current_time - start_time > total_receive_duration:
                break

            data_bytes, addr = udp_socket.recvfrom(2048)
            received_data = pickle.loads(data_bytes)

            # print(received_data, flush=True)  # NOTE THE FLUSH

            avg_delay += (time.time() - received_data['real_time']) * 1000  # unit: ms
            receive_cnt += 1

            if current_time - last_time >= 1.0:
                now_expected_receive_cnt = expected_receive_cnt * (current_time - start_time) / total_send_duration
                now_drop_rate = (1 - receive_cnt / now_expected_receive_cnt) * 100
                result_dict_list.append({
                    "time": f"{current_time - start_time: .1f}", 
                    "now drop rate": f"{now_drop_rate: .1f}%"
                    # "now expected": f"{now_expected_receive_cnt}",
                    # "now received": f"{receive_cnt}"
                })
                last_time = current_time
                
        except socket.timeout:
            continue

    if receive_cnt == 0:
        avg_delay = 0x3f3f3f3f
    else:
        avg_delay /= receive_cnt
    drop_rate = (1 - receive_cnt / expected_receive_cnt) * 100
    result_dict_list.append({"drop rate": f"{drop_rate: .1f}%", "delay": f"{avg_delay: .1f}"})
    
    print(json.dumps(result_dict_list, indent=2))

    # print('receiving stopped', flush=True)

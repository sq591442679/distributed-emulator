import socket
import sys
import time
import pickle

if __name__ == '__main__':
    target_ip = str(sys.argv[1])
    target_port = int(sys.argv[2])
    send_interval = float(sys.argv[3])          # unit: s
    total_send_duration = float(sys.argv[4])    # unit: s
    simulation_start_time = float(sys.argv[5])	# real time when simulation (i.e. link event) starts

    cnt = 0
    start_time = time.time()					# real time when sending starts

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print('sending UDP to ' + target_ip, flush=True)

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= total_send_duration:
            break

        cnt += 1
        data_dict = {
            'cnt': cnt,
            'sim-time': current_time - simulation_start_time,
            'real-time': current_time,
            'redundant': b'\x00' * 941  # ensure that the UDP packet payload = 1024Bytes
        }
        # print('boot time:', time.time() - psutil.boot_time())
        
        data_bytes = pickle.dumps(data_dict)
        # print('data bytes: ', len(data_bytes))
        udp_socket.sendto(data_bytes, (target_ip, target_port))

        time.sleep(send_interval)

    udp_socket.close()

    print('sending stopped')

import threading
import time
import psutil
from Interface import Interface
from const_var import *
from scapy.all import *
from scapy.layers.inet import IP
from ELB import ELB, node_id, chi_to_chi_field


interface_dict = { name: Interface(name) for name in ['eth1', 'eth2', 'eth3', 'eth4'] }
last_monitor_time = time.time()
last_packets_received = psutil.net_io_counters(pernic=False).packets_recv
last_packets_sent = psutil.net_io_counters(pernic=False).packets_sent
last_total_qlen = 0																# unit: pkt


def start_timer(interface: Interface):
	current_total_qlen = 0                                                      # q(t) in Eq.1, unit: pkt
	total_queue_capacity = 0                                                    # Q_l in Eq.1, unit: pkt
	max_delay = 0.0                                                             # d in Eq.2, unit: ms
	current_packets_received = psutil.net_io_counters(pernic=False).packets_recv
	current_packets_sent = psutil.net_io_counters(pernic=False).packets_sent
	current_time = time.time()
	interval = (current_time - last_monitor_time) * 1000                        # unit: ms
	input_rate = (current_packets_received - last_packets_received) / interval  # I in Eq.1, unit: pkt per ms
	output_rate = (current_packets_sent - last_packets_sent) / interval         # O in Eq.1, unit: pkt per ms

	for name, interface in interface_dict.items():
		qlen, delay = interface.get_qlen_and_delay()
		
		if qlen is None or delay is None:               # interface is down
			continue
		
		current_total_qlen += qlen
		total_queue_capacity += interface.queue_capacity
		max_delay = max(max_delay, delay)

	delta_d = (total_queue_capacity - current_total_qlen) / (input_rate - output_rate)  # Eq.1, unit: ms
	p = min(1, (MONITOR_INTERVAL + max_delay) / delta_d)                        		# Eq.2, unit: 1
	beta = 1 - p                                                                		# Eq.3
	alpha = beta / 2                                                            		# Eq.4
	q_t_bsa = min(total_queue_capacity * beta + max_delay * (input_rate - output_rate), 
				  total_queue_capacity)													# Eq.5, unit: pkt
	new_input_rate = output_rate + \
					(q_t_bsa - total_queue_capacity * alpha) / TIME_RESIDE				# Eq.6, unit: pkt per ms
	chi = min(max(0, new_input_rate / input_rate), 1)									# Eq.7

	send_elb_packet(chi)

	last_monitor_time = current_time
	last_packets_received = current_packets_received
	last_packets_sent = current_packets_sent

	print(time.time())
	threading.Timer(interface.monitor_interval / 1000, start_timer).start()


def send_elb_packet(chi: float):
	elb_packet = IP(dst="255.255.255.255", proto=ELB_PROTOCOL_NUMBER) / ELB(id=node_id, chi=chi_to_chi_field(chi))
	send(elb_packet)

if __name__ == '__main__':
	bind_layers(IP, ELB, proto=ELB_PROTOCOL_NUMBER)		# unassigned protocol number by IANA
	interface_eth1 = Interface('eth1')
	start_timer(interface_eth1)
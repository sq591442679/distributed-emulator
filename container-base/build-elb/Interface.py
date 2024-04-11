import psutil
import os
from pyroute2 import IPRoute

class Interface:
	def __init__(self, name: str) -> None:
		self.name = name
		self.packets_received = psutil.net_io_counters(pernic=True)[self.name].packets_recv
		self.packet_sent = psutil.net_io_counters(pernic=True)[self.name].packets_sent
		self.queue_capacity = int(os.environ.get('ELB_QUEUE_CAPACITY'))						# Q_l in eq.1 in ELB paper

	def __hash__(self) -> int:
		return hash(self.name)
    
	def calculate_delta_d(self):
		self.packets_received = psutil.net_io_counters(pernic=True)[self.name].packets_recv
		self.packet_sent = psutil.net_io_counters(pernic=True)[self.name].packets_sent
		qlen = 
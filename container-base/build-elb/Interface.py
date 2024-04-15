import psutil
import os
import time
from const_var import *
from pyroute2 import IPRoute
from typing import List, Tuple


class Interface:
	def __init__(self, name: str) -> None:
		self.name = name
		self.monitor_interval = MONITOR_INTERVAL						# parameter delta in ELB, unit: ms
		self.time_reside = TIME_RESIDE									# parameter theta in ELB, unit: ms
		self.queue_capacity = int(os.environ.get('QUEUE_CAPACITY'))		# Q_l in eq.1 in ELB paper

		self.last_monitor_time = time.time()							# unit: sec
		self.last_packets_received = 0									# unit: pkt
		self.last_packets_sent = 0										# unit: pkt


	def __hash__(self) -> int:
		return hash(self.name)
	

	def get_qlen_and_delay(self):
		"""
		returns qlen (pkts) and delay (ms)
		"""
		with IPRoute() as ipr:
			indeces = ipr.link_lookup(ifname=self.name)

			if len(indeces) == 0:
				return None, None
			
			idx = ipr.link_lookup(ifname=self.name)[0]
			qdiscs = ipr.get_qdiscs(index=idx)

			for qdisc in qdiscs:
				attrs = dict(qdisc['attrs'])
				if 'TCA_KIND' in attrs and attrs['TCA_KIND'] == 'netem':
					tca_options: dict = attrs['TCA_OPTIONS']
					delay: float = tca_options['delay'] / 1000

					tca_stats2: dict = attrs['TCA_STATS2']
					attrs: List[Tuple] = tca_stats2['attrs']
					for attr in attrs:
						if attr[0] == 'TCA_STATS_QUEUE':
							qlen: int = attr[1]['qlen']
		
		return qlen, delay


if __name__ == '__main__':
	interface = Interface('eth1')
	interface.calculate_and_monitor()


	{
		'TCA_KIND': 'netem', 
		'TCA_OPTIONS': {
			'delay': 230281, 'limit': 10000, 'loss': 0, 'gap': 0, 'duplicate': 0, 'jitter': 0, 'attrs': [('UNKNOWN', {'header': {'length': 12, 'type': 10}}), ('UNKNOWN', {'header': {'length': 12, 'type': 11}}), ('TCA_NETEM_CORR', {'delay_corr': 0, 'loss_corr': 0, 'dup_corr': 0}), ('TCA_NETEM_REORDER', {'prob_reorder': 0, 'corr_reorder': 0}), ('TCA_NETEM_CORRUPT', {'prob_corrupt': 0, 'corr_corrupt': 0}), ('TCA_NETEM_RATE', {'rate': 1250000000, 'packet_overhead': 0, 'cell_size': 0, 'cell_overhead': 0})]
		}, 
  		'UNKNOWN': {
			  'header': {'length': 5, 'type': 12}
		}, 
		'TCA_STATS2': {
			'attrs': [
				('TCA_STATS_BASIC', {'bytes': 39294, 'packets': 329}), 
				('TCA_STATS_QUEUE', {'qlen': 0, 'backlog': 0, 'drops': 0, 'requeues': 0, 'overlimits': 0})
			]
		}, 
		'TCA_STATS': {
			'bytes': 39294, 'packets': 329, 'drop': 0, 'overlimits': 0, 'bps': 0, 'pps': 0, 'qlen': 0, 'backlog': 0
		}
	}
import socket
import struct
from scapy.all import *
from scapy.layers.inet import IP
from ELB import ELB
from const_var import *


def create_netlink_socket():
	sock = socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, socket.NETLINK_USERSOCK)
	sock.bind((os.getpid(), 0))
	return sock


def send_to_kernel(sock: socket.socket, chi_field: int, ifindex: int):
	"""
	send a interval chi_field to kernel
	in kernel it should be converted to double
	"""
	message = struct.pack("If", ifindex, chi_field)
	sock.sendto(message, (0, 0))


def handle_elb_packet(packet: Packet):
	if ELB in packet:
		chi_field = int(packet[ELB].chi)
		ifindex = packet.sniffed_on
		send_to_kernel(sock, chi_field, ifindex)




if __name__ == '__main__':	
	bind_layers(IP, ELB, proto=ELB_PROTOCOL_NUMBER)		# unassigned protocol number by IANA
	sock = create_netlink_socket()
	sniff(filter=f"ip proto {ELB_PROTOCOL_NUMBER}", prn=handle_elb_packet)
	# print(socket.NETLINK_USERSOCK)
	sock.close()
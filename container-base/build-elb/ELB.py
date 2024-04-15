from scapy.all import *
import os
from scapy.layers.inet import IP
from const_var import *


class ELB(Packet):
	name = "ELB"
	fields_desc = [IntField("id", 0), IntField("chi", 0)]
	# NOTE: in ELB packet, the "chi" filed is an int32, representing chi * 10000
	# if chi < 0, then it is a warning signal and chi doesn't make sense


def chi_to_chi_field(chi: float) -> int:
	return round(chi * 10000)


ip3 = int(os.getenv("NODE_X"))
ip4 = int(os.getenv("NODE_Y"))
# ip3 = 255
# ip4 = 255
node_id = (ip4 << 24) | (ip3 << 16) | 0

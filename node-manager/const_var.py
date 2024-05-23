# BROADCAST PARAMETERS
import os
from datetime import datetime
from typing import List, Tuple

LATITUDE_KEY = 'lat'
LONGITUDE_KEY = 'lon'
HEIGHT_KEY = 'hei'
R_EARTH = 6371000       # unit: m
HOST_PREFIX_LEN = 16

# BROAD_CAST_SEND_INTERVAL
BROADCAST_SEND_INTERVAL = 3

WD = os.getcwd()
# VOLUME1
VOLUME1 = "%s/../configuration:/configuration"%WD
VOLUME2 = "/tmp/.X11-unix:/tmp/.X11-unix"
V_EDIT = "%s/../satellite_node_docker/video_trans:/edit"%WD
        
# LIGHT_SPEED
LIGHT_SPEED = 3e8       # unit: m/s

# DELAY BANDWIDTH LOSS
NETWORK_DELAY = 60      # unit ms, 150 means 150ms
NETWORK_BANDWIDTH = 10000 # unit Mbps
NETWORK_LOSS = 0        # percent 0 means 0%
QUEUE_CAPACITY = 10000    # unit: pkt

# CONSTELLATION PARAMETERS
ORBIT_NUM = 4
SAT_PER_ORBIT = 4
USE_WALKER_DELTA = False		# if True, then no seam
INCLINE_DEGREE: float = 89	
# note that in particular, when USE_WALKER_DELTA is False, INCLINE_DEGREE is usually near 90
USE_STATIC_POSITION = True

# SUBMISSION SIZE
SUBMISSION_SIZE_FOR_NETWORK_OBJECT_CREATION = 5
SUBMISSION_SIZE_FOR_NETWORK_CREATION = 10           # a larger value to help prevent "Read timeout" error
SUBMISSION_SIZE_FOR_CONTAINER_CREATION = 3
SUBMISSION_SIZE_FOR_DELETE_CONTAINER = 3
SUBMISSION_SIZE_FOR_DELETE_NETWORK = 4
SUBMISSION_SIZE_FOR_UPDATE_NETWORK_DELAY = 1

# LINK FAILURE
# NOTE: about the SIMULATION_DURATION, it should consider OSPF_LSA_MAXAGE and arp aging time
LINK_FAILURE_DURATION = 5       # unit: s
SIMULATION_DURATION = 100      # unit: s, better do not exceed OSPF_LSA_MAXAGE (3600)

# TRANSMISSION PAIR
SENDER_NODE_ID_LIST: List[Tuple[int, int]] = [(0, 1)]
RECEIVER_NODE_ID = (2, 2)
# SENDER_NODE_ID_LIST: List[Tuple[int, int]] = []
# RECEIVER_NODE_ID = (0, 0)

# used for tle generation and position update
TIME_BASE = datetime(2024, 1, 1)

UDP_SEND_INTERVAL = 0.01
DRY_RUN = True
WARMUP_PERIOD = 3000000      # unit: s
RANDOM_SEED_NUM = 5     # number of tests with different random seeds

RECORD_LONG_TERM_RESULT = True

LOFI_DELTA = 1.0
LINK_FAILURE_RATE_LIST = [0.05]
# PROTOCOL_LIST = [f"lofi(3-{LOFI_DELTA:.3f})"]
PROTOCOL_LIST = ["node_rule_bfs"]
TEST_NUMS = [1]
RANDOM_SEEDS = [451]
PROTOCOL_RELATED_ARGS = {
	"ospf": {
		"image_name": "ospf:latest",
		"modules_before_constellation_creation": [
			"./sqsq-kernel-modules/install_satellite_id.sh",
		],
		"modules_after_constellation_creation": [

		],
		"frr_configurations": [

		],
	},
	"node_rule_id": {
		"image_name": "node_rule_id:latest",
		"modules_before_constellation_creation": [
			"./sqsq-kernel-modules/install_satellite_id.sh",
		],
		"modules_after_constellation_creation": [
			"./sqsq-kernel-modules/install_multipath.sh",
		],
		"frr_configurations": [
			f"ospf orbit_num {ORBIT_NUM}",
			f"ospf sat_per_orbit {SAT_PER_ORBIT}",
			f"ospf use_walker_delta {int(USE_WALKER_DELTA)}",
		]
	},
	"node_rule_bfs": {
		"image_name": "node_rule_bfs:latest",
		"modules_before_constellation_creation": [
			"./sqsq-kernel-modules/install_satellite_id.sh",
		],
		"modules_after_constellation_creation": [
			"./sqsq-kernel-modules/install_multipath.sh",
		],
		"frr_configurations": [
			f"ospf orbit_num {ORBIT_NUM}",
			f"ospf sat_per_orbit {SAT_PER_ORBIT}",
			f"ospf use_walker_delta {int(USE_WALKER_DELTA)}",
		]
	},
}
for lofi_n in range(10):
	PROTOCOL_RELATED_ARGS[f"lofi({lofi_n}-{LOFI_DELTA:.3f})"] = {
		"image_name": "lofi:latest",
		"modules_before_constellation_creation": [
			"./sqsq-kernel-modules/install_satellite_id.sh",
			"./sqsq-kernel-modules/install_load_awareness.sh",
		],
		"modules_after_constellation_creation": [
			"./sqsq-kernel-modules/install_multipath.sh",
		],
		"frr_configurations": [
			f"ospf lofi {lofi_n}"
			f"ospf warmup_period {WARMUP_PERIOD}"
		],
		"lofi_delta": LOFI_DELTA,
	}
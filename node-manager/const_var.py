# BROADCAST PARAMETERS
import os
from datetime import datetime
from typing import List, Tuple

LATITUDE_KEY = 'lat'
LONGITUDE_KEY = 'lon'
HEIGHT_KEY = 'hei'
R_EARTH = 6371000
HOST_PREFIX_LEN = 16

# BROAD_CAST_SEND_INTERVAL
BROADCAST_SEND_INTERVAL = 3
NETWORK_DELAY_UPDATE_INTERVAL = 30

WD = os.getcwd()
# VOLUME1
VOLUME1 = "%s/../configuration:/configuration"%WD
VOLUME2 = "/tmp/.X11-unix:/tmp/.X11-unix"
V_EDIT = "%s/../satellite_node_docker/video_trans:/edit"%WD
        
# LIGHT_SPEED
LIGHT_SPEED = 300

# DELAY BANDWIDTH LOSS
NETWORK_DELAY = 150 # unit ms, 150 means 150ms
NETWORK_BANDWIDTH = '10Mbit'
NETWORK_LOSS = 0 # percent 0 means 0%
QUEUE_CAPACITY = 100    # unit: pkt

# CONSTELLATION PARAMETERS
ORBIT_NUM = 6
SAT_PER_ORBIT = 11

# SUBMISSION SIZE
SUBMISSION_SIZE_FOR_NETWORK_OBJECT_CREATION = 5
SUBMISSION_SIZE_FOR_NETWORK_CREATION = 10           # a larger value to help prevent "Read timeout" error
SUBMISSION_SIZE_FOR_CONTAINER_CREATION = 3
SUBMISSION_SIZE_FOR_DELETE_CONTAINER = 3
SUBMISSION_SIZE_FOR_DELETE_NETWORK = 4
SUBMISSION_SIZE_FOR_UPDATE_NETWORK_DELAY = 1

# LINK FAILURE  added by sqsq
# NOTE: about the SIMULATION_DURATION, it should consider OSPF_LSA_MAXAGE and arp aging time
LINK_FAILURE_DURATION = 20      # unit: s
SIMULATION_DURATION = 1000      # unit: s

# TRANSMISSION PAIR added by sqsq
SENDER_NODE_ID_LIST: List[Tuple[int, int]] = [(3, 3)]
RECEIVER_NODE_ID = (5, 8)
# SENDER_NODE_ID_LIST: List[Tuple[int, int]] = []
# RECEIVER_NODE_ID = (0, 0)

# used for tle generation and position update
TIME_BASE = datetime(2024, 1, 1)

TEST_NUM = 5
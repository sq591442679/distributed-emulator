# BROADCAST PARAMETERS
import os

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
NETWORK_BANDWIDTH = 100 # unis kbytes/s must integer, 100 means 100kB/s
NETWORK_LOSS = 0 # percent 0 means 0%

# CONSTELLATION PARAMETERS
ORBIT_NUM = 4
SAT_PER_ORBIT = 11

# SUBMISSION SIZE
SUBMISSION_SIZE_FOR_NETWORK_OBJECT_CREATION = 1
SUBMISSION_SIZE_FOR_NETWORK_CREATION = 4
SUBMISSION_SIZE_FOR_CONTAINER_CREATION = 6
SUBMISSION_SIZE_FOR_DELETE_CONTAINER = 3
SUBMISSION_SIZE_FOR_DELETE_NETWORK = 4
SUBMISSION_SIZE_FOR_UPDATE_NETWORK_DELAY = 1

# LINK FAILURE  added by sqsq
LINK_FAILURE_RATE = 0.1
LINK_FAILURE_DURATION = 5   # unit: s
SIMULATION_END_TIME = 100  # unit: s
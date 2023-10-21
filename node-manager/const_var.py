# BROADCAST PARAMETERS
import threading

LATITUDE_KEY = 'lat'
LONGITUDE_KEY = 'lon'
HEIGHT_KEY = 'hei'
R_EARTH = 6371000
HOST_PREFIX_LEN = 16

# BROAD_CAST_SEND_INTERVAL
BROADCAST_SEND_INTERVAL = 3
NETWORK_DELAY_UPDATE_INTERVAL = 30

# VOLUME1
VOLUME1 = "/home/satellite-2/Workspace/distributed_simulation/satellite-source-routing/configuration:/configuration"
VOLUME2 = "/tmp/.X11-unix:/tmp/.X11-unix"
V_EDIT = "/home/satellite-2/Workspace/distributed_simulation/satellite-source-routing/satellite_node_docker/video_trans:/edit"
        
# LIGHT_SPEED
LIGHT_SPEED = 300

# DELAY BANDWIDTH LOSS
NETWORK_DELAY = 0
NETWORK_BANDWIDTH = "10Mbps"
NETWORK_LOSS = "0%"

# CONSTELLATION PARAMETERS
ORBIT_NUM = 5
SAT_PER_ORBIT = 6

# SUBMISSION SIZE
SUBMISSION_SIZE_FOR_NETWORK_OBJECT_CREATION = 1
SUBMISSION_SIZE_FOR_NETWORK_CREATION = 4
SUBMISSION_SIZE_FOR_CONTAINER_CREATION = 3
SUBMISSION_SIZE_FOR_DELETE_CONTAINER = 3
SUBMISSION_SIZE_FOR_DELETE_NETWORK = 4
SUBMISSION_SIZE_FOR_UPDATE_NETWORK_DELAY = 1


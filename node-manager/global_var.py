# all satellites
import threading
from collections import OrderedDict

satellites = []
network_dict = {}   # network key (str) -> class Network
satellite_map = {}  # tuple of satellite id -> class SatelliteNode
connect_order_map = OrderedDict()
interface_map = {}  # tuple of satellite id -> interface
ground_stations = []

def reinit_global_var():
    global satellites, network_dict, satellite_map, connect_order_map, interface_map, ground_stations
    satellites.clear()
    network_dict.clear()
    satellite_map.clear()
    connect_order_map.clear()
    interface_map.clear()
    ground_stations.clear()

# lock
interface_map_lock = threading.Lock()
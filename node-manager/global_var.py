# all satellites
import threading
from collections import OrderedDict

satellites = []
networks = {}
satellite_map = {}
connect_order_map = OrderedDict()
interface_map = {}
ground_stations = []

def reinit_global_var():
    global satellites, networks, satellite_map, connect_order_map, interface_map, ground_stations
    satellites.clear()
    networks.clear()
    satellite_map.clear()
    connect_order_map.clear()
    interface_map.clear()
    ground_stations.clear()

# lock
interface_map_lock = threading.Lock()
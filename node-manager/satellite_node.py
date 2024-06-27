from skyfield.api import load, EarthSatellite, wgs84
from datetime import datetime, timedelta
from global_var import satellites
from loguru import logger
import subprocess

from tools import *


# 用来进行位置计算的线程
def worker(now: datetime, range_start: int, range_end: int, res, send_pipe):
    """
    Calculate the position of the satellite
    :param send_pipe:
    :param res:
    :param range_start: the start index of the satellites that this thread should calculate
    :param range_end: the end index of the satellites that this thread should calculate
    """
    # calculated satellite nums
    calculated_satellites_num = range_end - range_start + 1
    # calculate the position of the satellites
    for i in range(range_start, range_end + 1):
        index_base = 3 * i
        # logger.info("%d %d %d %d"%(len(res),index_base,len(satellites),i))
        res[index_base], res[index_base + 1], res[index_base + 2] = satellites[i].get_next_position(now)
    send_pipe.send(calculated_satellites_num)


class SatelliteNode:

    def __init__(self, tle_info: tuple, node_id: tuple, container_name: str):
        self.orbit = tle_info[0][5:].split('_')[0]
        self.position = tle_info[0][5:].split('_')[1]
        self.satellite = EarthSatellite(tle_info[1], tle_info[2], tle_info[0])
        self.ts = load.timescale()
        self.node_id = node_id              # tuple of (orbit number, inner orbir order)
        self.container_name = container_name    # str of hex used for docker
        self.container_pid = subprocess.check_output(['docker', 'inspect', '--format', '{{.State.Pid}}', container_name]).decode().strip()
        self.topo = []
        self.host_ip = ''
        self.subnet_ip = {}  # {subnet_str: interface}

    def __str__(self):
        return 'node_' + str(self.node_id[0]) + '_' + str(self.node_id[1])

    def get_next_position(self, time_now: datetime):
        """
        Get the next position of the satellite
        :param time_now: the time now
        :return: the next position of the satellite (in degree and meter)
        """
        # 获取当前时间
        t = self.ts.utc(time_now.year, time_now.month, time_now.day,
                        time_now.hour, time_now.minute, time_now.second)
        # 计算卫星的地心坐标位置
        geocentric = self.satellite.at(t)
        position = geocentric.position.km  # 获取以公里为单位的位置坐标 (x, y, z)
        lat, lon = wgs84.latlon_of(geocentric)
        lat_degree = lat.degrees
        lon_degree = lon.degrees
        height = wgs84.height_of(geocentric).m
        return lat_degree, lon_degree, height


if __name__ == "__main__":
    pass

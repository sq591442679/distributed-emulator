from const_var import ORBIT_NUM, SAT_PER_ORBIT
import os

def ip_to_subnet(ip: str, prefix_len: int) -> str:
    # print(ip, prefix_len)
    sections = ip.split('.', -1)
    if len(sections) < 4:
        raise Exception("Incorrect Format")
    ip_int = (int(sections[0]) << 24) + (int(sections[1]) << 16) + (int(sections[2]) << 8) + int(sections[3])

    shift_num = 32 - prefix_len
    ip_int = ip_int >> shift_num
    ip_int = ip_int << shift_num
    return "%d.%d.%d.%d" % (
        ip_int // (1 << 24),
        ip_int // (1 << 16) % 256,
        ip_int // (1 << 8) % 256,
        ip_int % 256
    )

def ip_str_to_int(ip: str) -> int:
    ret = 0
    ip_list = ip.split('.')
    for net in ip_list:
        ret <<= 8
        ret |= int(net)
    return ret
# added by sqsq
# NOTE: x, y all begin from 0
def satellite_id_tuple_to_index(id: tuple) -> int:
    x = int(id[0])  # count of orbit number
    y = int(id[1])  # count of inner-orbit number
    index = x * SAT_PER_ORBIT + y
    return index


def satellite_index_to_id_tuple(index: int) -> tuple:
    x = index // ORBIT_NUM
    y = index % SAT_PER_ORBIT
    return (x, y)


def satellite_id_tuple_to_str(id: tuple) -> str:
    return 'node_' + str(id[0]) + '_' + str(id[1])


def satellite_str_to_id_tuple(str: str) -> tuple:
    return (int(str.split('_')[1]), int(str.split('_')[2]))


if __name__ == "__main__":
    # print(ip_to_subnet("172.17.0.3", 16))
    # print(ip_to_subnet("172.17.8.3", 24))
    # print(ip_to_subnet("172.17.9.3", 8))
    # print(ip_to_subnet("172.17.0.3", 15))
    print(ip_str_to_int("10.134.180.139"))
    pass
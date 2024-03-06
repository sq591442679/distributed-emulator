import docker
import os

iflink: str = os.popen(f"cat /sys/class/net/veth5d84e74/iflink").read().strip()

client = docker.from_env()

container = client.containers.get('node_0_0')

ret = container.exec_run(['sh', '-c', f"/get_ifindex.sh 25985"])

print(ret)
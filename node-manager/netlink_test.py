from pyroute2 import NetNS, IPRoute, netns
import subprocess

def disable_container_interface(container_name, interface_name):
    # 使用Docker CLI获取容器的PID，以便找到其网络命名空间
    # 注意：这需要在宿主机上有权限执行Docker命令
    container_pid = subprocess.check_output(['docker', 'inspect', '--format', '{{.State.Pid}}', container_name]).decode().strip()

    print(container_pid)

    # print(netns.pid_to_ns(container_pid, nspath='/var/run/docker/netns/'))

    # 容器的网络命名空间路径
    netns_path = f'/proc/{container_pid}/ns/net'

    print(netns_path)
    
    # 进入容器的网络命名空间
    with NetNS(netns_path) as ns:
        # 使用IPRoute在该命名空间中操作网络接口
        idx = ns.link_lookup(ifname=interface_name)[0]
        print(idx)
        ns.link('set', index=idx, state='up')

# 示例：关闭容器`container1`的`eth1`接口
disable_container_interface('node_4_0', 'eth4')

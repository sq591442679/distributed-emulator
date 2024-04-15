FROM ospf:latest

LABEL mantainer="sqsq" description="ELB image"

ENV container docker

RUN pip install psutil

COPY elb_server.py /elb_server.py
COPY Interface.py /Interface.py
RUN chmod 777 /elb_server.py \ 
    && chmod 777 /Interface.py

# copied from https://github.com/robertdebock/docker-ubuntu-systemd/blob/focal/Dockerfile
# Enable systemd.
# RUN apt-get update ; \
#     apt-get install -y systemd systemd-sysv kmod; \
#     apt-get clean ; \
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ; \
#     cd /lib/systemd/system/sysinit.target.wants/ ; \
#     ls | grep -v systemd-tmpfiles-setup | xargs rm -f $1 ; \
#     rm -f /lib/systemd/system/multi-user.target.wants/* ; \
#     rm -f /etc/systemd/system/*.wants/* ; \
#     rm -f /lib/systemd/system/local-fs.target.wants/* ; \
#     rm -f /lib/systemd/system/sockets.target.wants/*udev* ; \
#     rm -f /lib/systemd/system/sockets.target.wants/*initctl* ; \
#     rm -f /lib/systemd/system/basic.target.wants/* ; \
#     rm -f /lib/systemd/system/anaconda.target.wants/* ; \
#     rm -f /lib/systemd/system/plymouth* ; \
#     rm -f /lib/systemd/system/systemd-update-utmp*

# block some service from running
# added by sqsq
# RUN systemctl mask \
#     dev-hugepages.mount \
#     sys-fs-fuse-connections.mount \
#     sys-kernel-config.mount \
#     display-manager.service \
#     getty@.service \
#     systemd-logind.service \
#     systemd-remount-fs.service \
#     getty.target \
#     graphical.target \ 
#     systemd-journald.service \ 
#     systemd-timesyncd.service

# VOLUME [ "/sys/fs/cgroup" ]

# CMD ["/lib/systemd/systemd"]
# CMD ["/bin/bash", "-c", "while true; do :; done"]
CMD ["/bin/bash", "/monitor_network.sh"]

# maunally starting: 
# docker run \
#   --tty \
#   --privileged \
#   --volume /sys/fs/cgroup:/sys/fs/cgroup:ro \
#   robertdebock/ubuntu


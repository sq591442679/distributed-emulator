FROM ubuntu_python:latest

LABEL mantainer="sqsq" description="LoFi image"

ENV container docker

# install libnl
COPY libnl-src /libnl
RUN chmod -R 777 /libnl \
    && cd /libnl \ 
    && autoreconf -ivf \ 
    && ./configure --prefix=/usr \  
    && make -j$(nproc) \ 
    && make install -j$(nproc) \ 
    && make clean

# add frr users and groups
RUN groupadd -r -g 92 frr \ 
    && groupadd -r -g 85 frrvty \
    && adduser --system --ingroup frr --home /var/run/frr/ \
        --gecos "FRR suite" --shell /sbin/nologin frr \ 
    && usermod -a -G frrvty frr

# install frr-lofi 
COPY frr-frr-8.5.2.tar.gz /
RUN tar -xvf frr-frr-8.5.2.tar.gz \
    && mv /frr-frr-8.5.2 /frr \ 
    && chmod -R 777 /frr \
    && cd /frr \
    && ./bootstrap.sh \
    && ./configure \
        --prefix=/usr \
        --includedir=\${prefix}/include \
        --bindir=\${prefix}/bin \
        --sbindir=\${prefix}/lib/frr \
        --libdir=\${prefix}/lib/frr \
        --libexecdir=\${prefix}/lib/frr \
        --localstatedir=/var/run/frr \
        --sysconfdir=/etc/frr \
        --with-moduledir=\${prefix}/lib/frr/modules \ 
        --enable-user=frr \
        --enable-group=frr \
        --enable-vty-group=frrvty \
        --enable-vtysh \ 
    && make -j$(nproc) \ 
    && make install -j$(nproc)
RUN cd /frr \ 
    && install -m 775 -o frr -g frr -d /var/log/frr \ 
    && install -m 775 -o frr -g frrvty -d /etc/frr \ 
    && install -m 640 -o frr -g frrvty tools/etc/frr/vtysh.conf /etc/frr/vtysh.conf \ 
    && install -m 640 -o frr -g frr tools/etc/frr/frr.conf /etc/frr/frr.conf \ 
    && install -m 640 -o frr -g frr tools/etc/frr/daemons.conf /etc/frr/daemons.conf \ 
    && install -m 640 -o frr -g frr tools/etc/frr/daemons /etc/frr/daemons \ 
    && install -m 644 tools/frr.service /etc/systemd/system/frr.service 
    # && systemctl enable frr
COPY resources/daemons /etc/frr/daemons
RUN echo "log file /var/log/frr/sqsq_ospfd.log" >> /etc/frr/frr.conf \
    && echo "log record-priority" >> /etc/frr/frr.conf \
    && echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf && sysctl -p

# copied from https://github.com/robertdebock/docker-ubuntu-systemd/blob/focal/Dockerfile
# Enable systemd.
RUN apt-get update ; \
    apt-get install -y systemd systemd-sysv kmod; \
    apt-get clean ; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ; \
    cd /lib/systemd/system/sysinit.target.wants/ ; \
    ls | grep -v systemd-tmpfiles-setup | xargs rm -f $1 ; \
    rm -f /lib/systemd/system/multi-user.target.wants/* ; \
    rm -f /etc/systemd/system/*.wants/* ; \
    rm -f /lib/systemd/system/local-fs.target.wants/* ; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev* ; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl* ; \
    rm -f /lib/systemd/system/basic.target.wants/* ; \
    rm -f /lib/systemd/system/anaconda.target.wants/* ; \
    rm -f /lib/systemd/system/plymouth* ; \
    rm -f /lib/systemd/system/systemd-update-utmp*

# block some service from running
# added by sqsq
RUN systemctl mask \
    dev-hugepages.mount \
    sys-fs-fuse-connections.mount \
    sys-kernel-config.mount \
    display-manager.service \
    getty@.service \
    systemd-logind.service \
    systemd-remount-fs.service \
    getty.target \
    graphical.target \ 
    systemd-journald.service \ 
    systemd-timesyncd.service

VOLUME [ "/sys/fs/cgroup" ]

CMD ["/lib/systemd/systemd"]

# ENTRYPOINT [ "/bin/bash" ]
# ENTRYPOINT [ "/sbin/init" ]
# CMD ["/lib/systemd/systemd"]

# maunally starting: 
# docker run \
#   --tty \
#   --privileged \
#   --volume /sys/fs/cgroup:/sys/fs/cgroup:ro \
#   robertdebock/ubuntu

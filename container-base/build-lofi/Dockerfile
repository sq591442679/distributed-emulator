FROM ubuntu_python:latest

LABEL mantainer="sqsq" description="LoFi image"

# install libnl
COPY libnl-src /libnl
RUN chmod -R 777 /libnl \
    && cd /libnl \ 
    && autoreconf -f -i \ 
    && ./configure --prefix=/usr \  
    && make -j$(nproc) \ 
    && make install -j$(nproc)

# add frr users and groups
RUN groupadd -r -g 92 frr \ 
    && groupadd -r -g 85 frrvty \
    && adduser --system --ingroup frr --home /var/run/frr/ \
        --gecos "FRR suite" --shell /sbin/nologin frr \ 
    && usermod -a -G frrvty frr

# install frr-lofi 
COPY frr-lofi-src /frr
RUN chmod -R 777 /frr \
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

# ENTRYPOINT [ "/bin/bash" ]
ENTRYPOINT [ "/sbin/init" ]

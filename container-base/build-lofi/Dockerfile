FROM ubuntu:20.04

LABEL mantainer="sqsq" description="LoFi image"

# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 以root用户权限进行登陆
USER root

# 替换为国内源
COPY resources/sources.list /etc/apt/sources.list

#Update the system and install required packages
RUN apt-get update -y \ 
    && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libncurses5-dev  \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    wget \
    libnetfilter-queue-dev \
    net-tools \
    iptables \
    vim \
    iputils-ping \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    xauth \
    tcpdump \ 
    grep \ 
    net-tools \ 
    iputils-ping \ 
    traceroute \ 
    iproute2 \ 
    systemd \ 
    systemd-sysv \ 
    dbus \ 
    dbus-user-session \ 
    git autoconf automake libtool make libreadline-dev texinfo \
    pkg-config libpam0g-dev libjson-c-dev bison flex \
    libc-ares-dev python3-dev python3-sphinx \
    install-info build-essential libsnmp-dev perl \
    protobuf-c-compiler libprotobuf-c-dev \
    libcap-dev libelf-dev libunwind-dev libpcre2-dev

RUN touch /root/.Xauthority \
    && xauth add unix:0.0 MIT-MAGIC-COOKIE-1  ed38891ce0eb40149fbdc76e11c94e76

# install libyang
RUN git clone https://github.com/CESNET/libyang.git \
    && cd libyang \
    && git checkout v2.1.128 \
    && mkdir build; cd build \
    && cmake -D CMAKE_INSTALL_PREFIX:PATH=/usr \
        -D CMAKE_BUILD_TYPE:String="Release" .. \
    && make \ 
    && make install
ENV LDFLAGS="-Wl,--copy-dt-needed-entries" 
# ENV LD_LIBRARY_PATH='$LD_LIBRARY /usr/local/lib'

# install libnl
COPY libnl-src /libnl
RUN chmod -R 777 /libnl \ 
    && cd /libnl \ 
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

FROM ubuntu:20.04

LABEL mantainer="HeFan Zhang" description="Source routing"
# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# 以root用户权限进行登陆
USER root
# 替换为国内源
# RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
COPY resources/sources.list /etc/apt/sources.list
## Update the system and install required packages
RUN apt-get update -y
RUN apt-get install -y \
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
    # systemd \ 
    # systemd-sysv \ 
    # dbus \ 
    # dbus-user-session \ 
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

# 启用ipv4转发
RUN echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf && sysctl -p

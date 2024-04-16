FROM ubuntu_python:latest

LABEL mantainer="sqsq" description="satellite base image"

ENV container docker

RUN apt-get update -y
RUN apt-get install -y kmod

# install libnl
COPY libnl-src /libnl
RUN chmod -R 777 /libnl \
    && cd /libnl \ 
    && autoreconf -ivf \ 
    && ./configure --prefix=/usr \  
    && make -j$(nproc) \ 
    && make install -j$(nproc) \ 
    && make clean

COPY ./udp-applications/ /udp-applications
COPY get_ifindex.sh /get_ifindex.sh
COPY monitor_network.sh /monitor_network.sh
COPY change_ospf_cost.sh /change_ospf_cost.sh
COPY ./set-satellite-id/ /set-satellite-id

RUN chmod -R 777 /udp-applications \ 
    && chmod 777 /get_ifindex.sh \ 
    && chmod 777 /monitor_network.sh \ 
    && chmod -R 777 /change_ospf_cost.sh \ 
	&& chmod -R 777 /set-satellite-id \ 
	&& /set-satellite-id/compile.sh
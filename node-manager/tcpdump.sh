#!/bin/bash

interfaces=$(ls /sys/class/net/ | grep '^br-')
sudo tcpdump $(echo $interfaces | sed 's/[^ ]*/-i &/g') -w capture.pcap
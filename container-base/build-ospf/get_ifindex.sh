#!/bin/bash

# $1: target ifindex
# output: path of an interface which ifindex == $1
# i.e., /sys/class/net/eth1/ifindex
grep -l $1 /sys/class/net/*/ifindex
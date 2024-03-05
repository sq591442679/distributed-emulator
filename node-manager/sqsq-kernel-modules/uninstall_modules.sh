# !/bin/bash

currentpath=$(dirname "$(readlink -f "$0")")
echo 'shanqian' | sudo -S rmmod load_awareness_module
sudo rmmod multipath_module
cd $currentpath/load_awareness_module
make clean
cd $currentpath/multipath_module
make clean
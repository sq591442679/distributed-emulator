# !/bin/bash

currentpath=$(dirname "$(readlink -f "$0")")
echo 'shanqian' | sudo -S rmmod load_awareness_module
sudo rmmod multipath_module
sudo rmmod packet_drop_module
sudo rmmod satellite_id_module
cd $currentpath/load_awareness_module
make clean
cd $currentpath/multipath_module
make clean
cd $currentpath/packet_drop_module
make clean
cd $currentpath/satellite_id_module
make clean
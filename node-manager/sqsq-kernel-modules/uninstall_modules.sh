# !/bin/bash

echo 'shanqian' | sudo -S rmmod load_awareness_module
sudo rmmod multipath_module
cd ./load_awareness_module
make clean
cd ../multipath_module
make clean
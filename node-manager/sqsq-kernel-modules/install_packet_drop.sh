# !/bin/bash

currentpath=$(dirname "$(readlink -f "$0")")

# ./compile_kernel.sh

cd $currentpath/packet_drop_module

make -j$(nproc)
echo 'shanqian' | sudo -S insmod packet_drop_module.ko
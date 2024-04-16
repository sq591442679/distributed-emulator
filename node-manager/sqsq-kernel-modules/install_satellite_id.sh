# !/bin/bash

currentpath=$(dirname "$(readlink -f "$0")")

# ./compile_kernel.sh

cd $currentpath/satellite_id_module

make -j$(nproc)
echo 'shanqian' | sudo -S insmod satellite_id_module.ko
# !/bin/bash

currentpath=$(dirname "$(readlink -f "$0")")

# ./compile_kernel.sh

cd $currentpath/multipath_module

make -j$(nproc)
echo 'shanqian' | sudo -S insmod multipath_module.ko
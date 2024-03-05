# !/bin/bash

currentpath=$(dirname "$(readlink -f "$0")")

# ./compile_kernel.sh

cd $currentpath/load_awareness_module

make 
echo 'shanqian' | sudo -S insmod load_awareness_module.ko
#!/bin/bash

start_time=$(date +%s)

cd /home/sqsq/Desktop/linux-5.15.132-sqsq
echo ""
echo 'compiling, please wait...'
echo 'shanqian' | sudo -S make -j$(nproc) 2>&1 | grep -E 'error:|warning:'
sudo make -j$(nproc) INSTALL_MOD_STRIP=1 modules_install 2>&1 | grep -E 'error:|warning:'
sudo make install 2>&1 | grep -E 'error:|warning:'  # only print warning and errors on terminal
sudo update-grub > /dev/null

end_time=$(date +%s)

execution_time=$((end_time - start_time))

echo "execution time: $execution_time"
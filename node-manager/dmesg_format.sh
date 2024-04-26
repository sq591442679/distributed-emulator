#!/bin/bash

# 获取系统启动时间（秒）
btime=$(awk '/btime/ {print $2}' /proc/stat)

# 处理dmesg输出
dmesg -c | while read line; do
    # 检查行是否不包含子串 'entered'
    if ! echo "$line" | grep -q "veth"; then
        # 提取时间戳（秒）
        timestamp=$(echo $line | awk '{print substr($1, 2, length($1)-2)}')
        
        # 将启动时间和时间戳相加，并转换为自epoch以来的时间（秒）
        epoch_time=$(echo "$btime + $timestamp" | bc)
        
        # 输出epoch时间和原始日志
        echo "[$epoch_time]$(echo $line | cut -d']' -f2-)"
    fi
done

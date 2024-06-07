#!/bin/bash

# 运行10次循环
for i in {1..10}
do
  # 关闭网络接口eth1
  echo "Closing eth1... (Cycle $i)"
  ifconfig eth1 down
  sleep 5

  # 开启网络接口eth1
  echo "Opening eth1... (Cycle $i)"
  ifconfig eth1 up
  sleep 5
done

echo "Completed 10 cycles of opening and closing eth1."

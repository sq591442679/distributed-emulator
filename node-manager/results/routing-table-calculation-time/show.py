"""
monitor node_2_3 and change eth1 of node_3_7,15*15 satellites
"""

import matplotlib.pyplot as plt
import os
import re

# 读取CSV文件
metric = 'delay'
current_path = os.path.dirname(__file__)
protocol_names = ['id', 'bfs', 'ospf']
result_path_prefix = f'{current_path}/{metric}'
file_names = [f'{result_path_prefix}/{protocol}.log' for protocol in protocol_names]
average_execution_time = []
average_pure_calculation_time = []
average_other_time = []

for file_name in file_names:
	# print(file_name)
	with open(file_name, 'r') as file:
		log_content = file.read()
		excecution_times = re.findall(r'calculation, elapsed (\d+)ns,(\d+)ns', log_content)
		first_parts = [int(times[0]) for times in excecution_times]
		second_parts = [int(times[1]) for times in excecution_times]
		average_first = sum(first_parts) / len(first_parts) / 1000					# uint: μs
		average_second = sum(second_parts) / len(second_parts) / 1000				# uint: μs

		average_execution_time.append(average_first)
		average_pure_calculation_time.append(average_second)
		average_other_time.append(average_first - average_second)

print(average_execution_time, average_pure_calculation_time, average_other_time)

# 设置颜色
# default_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
# color_cycle = cycle(default_colors)

# 绘制堆叠柱状图
plt.figure(figsize=(10, 10))
bar_width = 0.3

# 绘制柱状图
bars1 = plt.bar(protocol_names, 
				average_other_time, 
				bottom=average_pure_calculation_time, 
				label='Other Time',
				color='none', 
				edgecolor='C0',
				hatch='++',
				linewidth=3)
bars2 = plt.bar(protocol_names, 
				average_pure_calculation_time, 
				label='Pure Calculation Time',
				color='none', 
				edgecolor='C1',
				hatch='//',
				linewidth=3)

# 添加标题和标签，增大字号
plt.title('Routing Table Calculation Time of 15*15 Satellites', fontsize=20)
# plt.xlabel('Protocol', fontsize=16)
plt.ylabel('Average Time (μs)', fontsize=18)
plt.xlabel('Protocol', fontsize=18)
plt.ylim(0, 2200)

# 设置刻度的字号
plt.xticks(rotation=0, fontsize=18)
plt.yticks(fontsize=14)
# plt.ylim(0, 900)

# 添加图例
plt.legend(fontsize=14)

# 显示图表
# plt.savefig(f'{result_path_prefix}/result.pdf', format='pdf')
# plt.show()
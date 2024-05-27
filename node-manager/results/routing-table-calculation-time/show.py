import pandas as pd
import matplotlib.pyplot as plt
import os
from itertools import cycle

# 读取CSV文件
current_path = os.path.dirname(__file__)
df = pd.read_csv(f'{current_path}/result.csv')

# 过滤掉protocol字段为'comment'的行
df_filtered = df[df['protocol'] != 'comment']

# 移除'execution_time'和'pure_calculation_time'中的'ns'后缀并转换为浮点数，然后从纳秒转换为微秒
df_filtered['execution_time'] = df_filtered['execution_time'].str.replace('ns', '').astype(float) / 1000
df_filtered['pure_calculation_time'] = df_filtered['pure_calculation_time'].str.replace('ns', '').astype(float) / 1000

# 计算每个协议的平均执行时间和平均纯计算时间（单位为微秒）
average_execution_time = df_filtered.groupby('protocol')['execution_time'].mean()
average_pure_calculation_time = df_filtered.groupby('protocol')['pure_calculation_time'].mean()

# 按照所需的顺序重新排序
desired_order = ['node-rule-bfs', 'node-rule-id', 'ospf']
average_execution_time = average_execution_time.reindex(desired_order)
average_pure_calculation_time = average_pure_calculation_time.reindex(desired_order)

# 设置颜色
# default_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
# color_cycle = cycle(default_colors)

# 绘制堆叠柱状图
plt.figure(figsize=(10, 10))
bar_width = 0.4

# 绘制柱状图
bars1 = plt.bar(desired_order, average_execution_time, color='C0', label='Other Time')
bars2 = plt.bar(desired_order, average_pure_calculation_time, color='C1', bottom=average_execution_time - average_pure_calculation_time, label='Pure Calculation Time')

# 添加标题和标签，增大字号
plt.title('Average Execution Time and Pure Calculation Time', fontsize=20)
plt.xlabel('Protocol', fontsize=16)
plt.ylabel('Average Time (μs)', fontsize=16)

# 设置刻度的字号
plt.xticks(rotation=0, fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0, 900)

# 添加图例
plt.legend()

# 显示图表
plt.show()
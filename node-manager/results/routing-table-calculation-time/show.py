import pandas as pd
import matplotlib.pyplot as plt
import os
from itertools import cycle

# 读取CSV文件
current_path = os.path.dirname(__file__)
df = pd.read_csv(f'{current_path}/result.csv')

# 过滤掉protocol字段为'comment'的行
df_filtered = df[df['protocol'] != 'comment']

# 移除'execution_time'中的'ns'后缀并转换为浮点数，然后从纳秒转换为微秒
df_filtered['execution_time'] = df_filtered['execution_time'].str.replace('ns', '').astype(float) / 1000

# 计算每个协议的平均执行时间（单位为微秒）
average_times = df_filtered.groupby('protocol')['execution_time'].mean()

# 获取matplotlib的默认颜色
default_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
color_cycle = cycle(default_colors)

# 绘制柱状图
plt.figure(figsize=(10, 10))
average_times.plot(kind='bar', color=[next(color_cycle) for _ in range(len(average_times))])

# 添加标题和标签，增大字号
plt.title('Average Execution Time of Different Protocols', fontsize=25)
plt.xlabel('Protocol', fontsize=22)
plt.ylabel('Average Execution Time (μs)', fontsize=22)

# 设置刻度的字号
plt.xticks(rotation=0, fontsize=18)
plt.yticks(fontsize=18)

# 显示图表
plt.show()

import os
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
current_directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(f'{current_directory}/result.csv')

# 提取数据
n = df['n']
convergency_time = df['convergency_time']
total_overhead = df['total_overhead']

# 创建画布和子图
fig, ax1 = plt.subplots()

# 绘制左轴数据，使用第一个默认颜色
ax1.plot(n, convergency_time * 1000, 'o-', label='convergency time', color=plt.get_cmap('tab10').colors[0])
ax1.set_xlabel('n')
ax1.set_ylabel('convergency time (ms)')
ax1.set_ylim(3, 19)
ax1.grid()
ax1.set_xticks([2, 3, 4, 5])

# 创建一个右轴对象
ax2 = ax1.twinx()
# 绘制右轴数据，使用第二个默认颜色
ax2.plot(n, total_overhead / 1000, 'o-', label='control overhead', color=plt.get_cmap('tab10').colors[1])
ax2.set_ylabel('control overhead (KBytes)')
ax2.set_ylim(0, 80)
ax2.grid()
ax2.set_xticks([2, 3, 4, 5])

# 添加图例
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 显示图形
plt.tight_layout()
# plt.grid()
plt.title('Convergency Time and Total Overhead vs. n')
plt.show()

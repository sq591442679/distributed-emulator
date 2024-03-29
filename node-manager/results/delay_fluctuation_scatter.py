import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as ticker

# 读取CSV文件
current_path = os.path.dirname(__file__)
df = pd.read_csv(current_path + "/result_fluctuation.csv")

df['delay'] = df['delay']  # 无需转换数据格式

# 筛选出link_failure_rate为0、0.01、0.05的数据
filtered_df = df[df['link_failure_rate'].isin([0, 0.01, 0.05])]

# 重置颜色循环，使用默认颜色
plt.gca().set_prop_cycle(None)

# 定义颜色浅一点的版本
colors_lighter = ['tab:blue', 'tab:orange', 'tab:green']

# 绘制散点图和色块
for idx, (name, group) in enumerate(filtered_df.groupby('link_failure_rate')):
    # 计算每个数据点的上下范围
    max_val = group['delay'].max() + 0.005
    min_val = group['delay'].min() - 0.005
    
    # 绘制散点图
    plt.scatter(range(1, len(group) + 1), group['delay'], label=f'link failure rate={name * 100}%', zorder=2)
    
    # 绘制色块
    plt.fill_between(range(0, 12), min_val, max_val, color=colors_lighter[idx], alpha=0.3, zorder=1)

plt.xlabel('Experiment Index')
plt.ylabel('Delay')
plt.title('Delay vs. Experiment Index')
plt.legend()
plt.xlim(0, 11)    # 设置横坐标范围
plt.ylim(100, 120)
plt.grid(True, zorder=3)  # 设置网格线zorder为3，使其位于色块下方

plt.show()

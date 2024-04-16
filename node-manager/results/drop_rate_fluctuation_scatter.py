import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as ticker

# 读取CSV文件
current_path = os.path.dirname(__file__)
df = pd.read_csv(current_path + "/result_fluctuation.csv")

df['drop_rate'] = df['drop_rate'].str.rstrip('%').astype('float') / 100

# 筛选出link_failure_rate为0、0.01、0.05的数据
filtered_df = df[df['link_failure_rate'].isin([0, 0.01, 0.05])]

# 重置颜色循环，使用默认颜色
plt.gca().set_prop_cycle(None)

# 定义颜色浅一点的版本
colors_lighter = ['tab:blue', 'tab:orange', 'tab:green']

# 绘制散点图和色块
for idx, (name, group) in enumerate(filtered_df.groupby('link_failure_rate')):
    # 计算每个数据点的上下范围
    max_val = group['drop_rate'].max() + 0.0002
    min_val = group['drop_rate'].min() - 0.0002
    
    # 绘制散点图
    plt.scatter(range(1, len(group) + 1), group['drop_rate'], label=f'link failure rate={name * 100}%', zorder=2)
    
    # 绘制色块
    plt.fill_between(range(0, 12), min_val, max_val, color=colors_lighter[idx], alpha=0.3, zorder=1)

plt.xlabel('Experiment Index')
plt.ylabel('Drop Rate')
plt.title('Drop Rate vs. Experiment Index')
plt.legend()
plt.ylim(0, 0.1)  # 设置纵坐标范围
plt.xlim(0, 11)    # 设置横坐标范围
plt.grid(True, zorder=3)  # 设置网格线zorder为3，使其位于色块下方
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import FuncFormatter

current_path = os.path.dirname(__file__)
# 读取CSV文件
df = pd.read_csv(current_path + '/result.csv')

df['drop_rate'] = df['drop_rate'].str.rstrip('%').astype('float') / 100

# 不同 lofi_n 值的范围
lofi_n = 2
random_seeds = [42, 43, 44, 45, 46]

def to_percent(tmp, position):
    return f'{tmp*100:.0f}%'

for i, random_seed in enumerate(random_seeds):
    title = f'66 satellites, 5% failure, n={lofi_n}, throughput over different seeds'
        
    # 筛选出对应 lofi_n 值的数据
    lofi_n_data = df[(df['random_seed'] == random_seed) & (df['lofi_n'] == lofi_n)]

    # 获取数据行数作为简单的编号
    id = [j + i * len(lofi_n_data) for j in range(1, len(lofi_n_data) + 1)]
    
    throughput = lofi_n_data['throughput']

    # 绘制散点图
    plt.scatter(id, throughput, color=f'C{i}', label=f'seed={random_seed}')
    plt.title(title)
    plt.ylabel('throughput (MBps)')
    plt.ylim(0.1, 0.2)
    
    plt.grid()

    plt.legend()
    
    # 修改纵坐标刻度标签
    plt.xticks([0, 10, 20, 30, 40, 50])
    plt.xlabel('tests')
    plt.xlim(left=0)
    # yticks = [0, 0.1, 0.2]
    # plt.yticks(yticks)
    # plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

# plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import os

current_path = os.path.dirname(__file__)
# 读取CSV文件
df = pd.read_csv(current_path + '/result.csv')

df['drop_rate'] = df['drop_rate'].str.rstrip('%').astype('float') / 100

# 不同 lofi_n 值的范围
# lofi_n_values = [1, 2, 3, 4, 5, -1]
lofi_n_values = [0, 1, 2, 3, 4, 5, 6, -1]

# 绘制多张子图
fig, axs = plt.subplots(4, 2, figsize=(12, 18))

for i, lofi_n in enumerate(lofi_n_values):
    title = f'lofi_n={lofi_n}: Drop Rate'
        
    # 筛选出对应 lofi_n 值的数据
    lofi_n_data = df[df['lofi_n'] == lofi_n]

    # 获取数据行数作为简单的编号
    id = range(1, len(lofi_n_data) + 1)
    drop_rate = lofi_n_data['drop_rate']
    
    mean_drop_rate = drop_rate.mean()
    

    # 绘制散点图
    ax = axs[i // 2, i % 2]
    ax.scatter(id, drop_rate, zorder=3)
    ax.axhline(mean_drop_rate, label=f'mean: {mean_drop_rate * 100 :.2f}%', linewidth=3,
               color=plt.rcParams['axes.prop_cycle'].by_key()['color'][1], zorder=4)
    ax.set_title(title)
    ax.set_xlabel('tests')
    ax.set_xlim(0, 100)
    ax.set_ylabel('drop rate')
    ax.set_ylim(0, 0.2)  # 设置y轴范围从0开始
    ax.grid(True)

    ax.spines['bottom'].set_zorder(2)
    ax.spines['left'].set_zorder(2)
    ax.spines['right'].set_zorder(2)
    
    ax.legend(loc='upper right')

# 调整子图间距
plt.subplots_adjust(hspace=0.8, wspace=0.3)

# plt.tight_layout()
plt.show()

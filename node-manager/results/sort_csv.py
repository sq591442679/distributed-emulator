import pandas as pd
import os

current_path = os.path.dirname(__file__)
# 读取CSV文件
df = pd.read_csv(current_path + '/result.csv')

lofi_n_orfer = [0, 1, 2, 3, 4, 5, 6, -1]

df['lofi_n'] = pd.Categorical(df['lofi_n'], categories=lofi_n_orfer, ordered=True)
df_sorted = df.sort_values('lofi_n')

df_sorted.to_csv(current_path + '/result.csv', index=False)
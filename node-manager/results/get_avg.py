import pandas as pd
import os

current_path = os.path.dirname(__file__)
df = pd.read_csv(f'{current_path}/result.csv')

def remove_outliers(series):
    mean = series.mean()
    std = series.std()
    threshold = 2
    return series[abs(series - mean) < threshold * std]

lofi_n_order = [0, 1, 2, 3, 4, 5 ,-1]
df['lofi_n'] = pd.Categorical(df['lofi_n'], categories=lofi_n_order, ordered=True)
df = df.sort_values('lofi_n')

for lofi_n, group in df.groupby('lofi_n'):
    print(f"lofi_n: {lofi_n}")
    
    filtered_drop_rate = remove_outliers(group['drop_rate'])
    filtered_df = group[group['drop_rate'].isin(filtered_drop_rate)]
    
    removed_df = group[~group['drop_rate'].isin(filtered_drop_rate)]
    if not removed_df.empty:
        print("filtered results:")
        print(removed_df[['drop_rate', 'delay']])
    
    mean_drop_rate = filtered_df['drop_rate'].mean()
    mean_delay = filtered_df['delay'].mean()
    print(f"rest avg drop_rate: {mean_drop_rate * 100 :.1f}%")
    print(f"rest avg delay: {mean_delay:.2f}\n")

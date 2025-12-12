import pandas as pd

df = pd.read_csv('data/input.csv')
total = len(df)
failures = (df['result'] == 'fail').sum()
rate = failures / total

with open('docs/metric.txt', 'w') as f:
    f.write(f'failed_login_rate={rate:.2f}\n')
print(f'failed_login_rate={rate:.2f}')

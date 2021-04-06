import pandas as pd
import numpy as np

# PandasのDataFrame型に変換
df = pd.read_csv('/Users/hogino/Documents/prog/python/nikkeisoftware/nsw202103vscode/t32103/VSC2/data/onsen-data.csv')

# データセットの先頭５件を表示
df.head()
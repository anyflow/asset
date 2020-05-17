# %%

from pandas_datareader import data as pdr
import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd

# %%
yf.pdr_override()


stock = 'VT'

start = dt.datetime(2019, 1, 1)

now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)

ma = 50

df['sma_{}'.format(ma)] = df.iloc[:, 4].rolling(window=ma).mean()

# print(df)
print(df.iloc[:])
# %%

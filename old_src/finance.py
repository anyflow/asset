# %%

import datetime as dt
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
from quantopian.research import prices, symbols

samsung_electronics = yf.Ticker('005930.KS')

samsung_electronics.info


# %%

# style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 5, 4)

# VT IAU EDV VCLT EMLC LTPZ DBC
df = web.DataReader('AIG', 'yahoo', start, end)
# print(df.head())

df['Adj Close'].plot()
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
# %%

# Research environment functions

# Pandas library: https://pandas.pydata.org/

# Query historical pricing data for AAPL
aapl_close = prices(
    assets=symbols('AAPL'),
    start='2013-01-01',
    end='2016-01-01',
)

# Compute 20 and 50 day moving averages on
# AAPL's pricing data
aapl_sma20 = aapl_close.rolling(20).mean()
aapl_sma50 = aapl_close.rolling(50).mean()

# Combine results into a pandas DataFrame and plot
pd.DataFrame({'AAPL': aapl_close, 'SMA20': aapl_sma20, 'SMA50': aapl_sma50}).plot(
    title='AAPL Close Price / SMA Crossover'
)

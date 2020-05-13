# %%

from quantopian.research import prices, symbols
import pandas_datareader.data as web
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import datetime as dt
import backtrader as bt
from datetime import datetime
import yfinance as yf

samsung_electronics = yf.Ticker('005930.KS')

samsung_electronics.info


# %%


# class SmaCross(bt.Strategy):  # bt.Strategy를 상속한 class로 생성해야 함.

#     params = dict(
#         pfast=5,  # period for the fast moving average
#         pslow=30  # period for the slow moving average
#     )

#     def __init__(self):
#         sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
#         sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
#         self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

#     def next(self):
#         if not self.position:  # not in the market
#             if self.crossover > 0:  # if fast crosses slow to the upside
#                 close = self.data.close[0]  # 종가 값
#                 size = int(self.broker.getcash() / close)  # 최대 구매 가능 개수
#                 self.buy(size=size)  # 매수 size = 구매 개수 설정
#         elif self.crossover < 0:  # in the market & cross to the downside
#             self.close()  # 매도


# cerebro = bt.Cerebro()  # create a "Cerebro" engine instance

# # 삼성전자의 '005930.KS' 코드를 적용하여 데이터 획득
# data = bt.feeds.YahooFinanceData(dataname='005930.KS',
#                                  fromdate=datetime(2019, 1, 1),
#                                  todate=datetime(2019, 12, 31))

# cerebro.adddata(data)
# cerebro.broker.setcash(1000000)  # 초기 자본 설정
# cerebro.broker.setcommission(commission=0.00015)  # 매매 수수료는 0.015% 설정

# cerebro.addstrategy(SmaCross)  # 자신만의 매매 전략 추가

# cerebro.run()  # 백테스팅 시작


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
pd.DataFrame({
    'AAPL': aapl_close,
    'SMA20': aapl_sma20,
    'SMA50': aapl_sma50
}).plot(
    title='AAPL Close Price / SMA Crossover'
)

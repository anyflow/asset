from datetime import datetime

from lib.backtrander_invoker import invoke

TICKERS = {
    'SAMSUNG': '005930.KS',
    'APPLE': 'AAPL',
    'TESLA': 'TSLA',
    'AMAZON': 'AMZN',
    'S&P500': 'SPY',
}


invoke(TICKERS['APPLE'], 1000000, datetime(1990, 1, 1))

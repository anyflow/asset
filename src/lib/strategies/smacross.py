import backtrader as bt


class SmaCross(bt.SignalStrategy):  # bt.Strategy를 상속한 class로 생성해야 함.
    params = {
        'pfast': 5,  # period for the fast moving average
        'pslow': 30  # period for the slow moving average
    }

    def __init__(self):
        self.dataclose = self.datas[0].close

        sma1 = bt.ind.SMA(period=self.params.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.params.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])

        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                close = self.data.close[0]  # 종가 값
                size = int(self.broker.getcash() / close)  # 최대 구매 가능 개수

                self.buy(size=size)  # 매수 size = 구매 개수 설정
            elif self.crossover < 0:  # in the market & cross to the downside
                self.close()  # 매도

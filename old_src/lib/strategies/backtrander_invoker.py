from datetime import datetime
import backtrader as bt


def invoke(ticker, cash, from_date, to_date=datetime.now(), commission=0.015 * 0.01):
    cerebro = bt.Cerebro()

    # 삼성전자의 '005930.KS' 코드를 적용하여 데이터 획득
    data = bt.feeds.YahooFinanceData(
        dataname=ticker, fromdate=from_date, todate=to_date
    )

    cerebro.adddata(data)
    cerebro.broker.setcash(cash)
    cerebro.broker.setcommission(commission=commission)
    # cerebro.addstrategy(SmaCross)  # 자신만의 매매 전략 추가

    cerebro.run()  # 백테스팅 시작

    cerebro.plot()  # 그래프로 보여주기

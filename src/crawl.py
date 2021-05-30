import csv
import io
import urllib
from datetime import datetime

from lib.http import request


def price() -> list:
    # http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020506 (종목시세)

    # 종목코드,종목명,시장구분,소속부,종가,대비,등락률,시가,고가,저가,거래량,거래대금,시가총액,상장주식수
    # "060310","3S","KOSDAQ","중견기업부","2905","10","0.35","2895","2925","2870","132202","383247855","134418745265","46271513"

    return __process('dbms/MDC/STAT/standard/MDCSTAT01501')


def company() -> list:
    # http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020506 (업종분류현황)

    # 종목코드,종목명,시장구분,업종명,종가,대비,등락률,시가총액
    # "095570","AJ네트웍스","KOSPI","서비스업","5880","90","1.55","275315094600"

    return __process('dbms/MDC/STAT/standard/MDCSTAT03901')


def __process(process_url: str) -> list:
    res = request(
        url='http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        method='POST',
        body=urllib.parse.urlencode(
            {
                'mktId': 'STK',
                'trdDd': datetime.now().strftime('%Y%m%d'),
                'money': 1,
                'csvxls_isNo': 'false',
                'name': 'fileDown',
                'url': process_url,
            }
        ),
    )

    res = request(
        url='http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        method='POST',
        body=f'code={res.body}',
        encoding='euc-kr',
    )

    return list(csv.DictReader(io.StringIO(res.body)))

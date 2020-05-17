

# %%
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd

from lib.mongodb import APARTMENTS
from address import address1s, address2s, address3s


# %%

# pprint(address1s())
pprint(address3s('경기도', '용인시 수지구'))
# %%

ADDR_1 = ['서울특별시',
          '부산광역시',
          '대구광역시',
          '인천광역시',
          '광주광역시',
          '대전광역시',
          '울산광역시',
          '세종특별자치시',
          '경기도',
          '강원도',
          '충청북도',
          '충청남도',
          '전라북도',
          '전라남도',
          '경상북도',
          '경상남도',
          '제주특별자치도']

SEOUL_ADDR_2 = ['종로구',
                '중구',
                '용산구',
                '성동구',
                '광진구',
                '동대문구',
                '중랑구',
                '성북구',
                '강북구',
                '도봉구',
                '노원구',
                '은평구',
                '서대문구',
                '마포구',
                '양천구',
                '강서구',
                '구로구',
                '금천구',
                '영등포구',
                '동작구',
                '관악구',
                '서초구',
                '강남구',
                '송파구',
                '강동구']

APARTMENTS.find({'address_1': '서울특별시', 'address_2': ''}).distinct('address_2')

# %%
ret = list(APARTMENTS.find({
    # 'address_2': '종로구',
    # 'exclusiveArea': 115.53
    'address_1': '경기도',
    'address_2': '용인시 수지구',
    # 'address_3': '성복동',
    # 'apartment': '벽산첼시빌2차'
}).sort('dealedAt', 1))  # .distinct('apartment'))  #


def del_id(obj):
    del obj['_id']
    del obj['__v']

    return obj


ret = list(map(del_id, ret))
ret_length = len(ret)


df = pd.DataFrame(ret)

df['평수'] = df['exclusiveArea'] / 3.3

grouped = df.groupby(['apartment', 'exclusiveArea']).max().reset_index()
byuk = df[df['apartment'] == '벽산첼시빌2차']


# x = list(o['dealedAt'] for o in ret)
# y = list(o['price'] for o in ret)

# plt.plot(x, y)

# for item in ret:
#     pprint(item)


# %%

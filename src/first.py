

# %%
from pymongo import MongoClient
from pprint import pprint

import matplotlib.pyplot as plt

client = MongoClient('mongodb://localhost')

dbs = client.database_names();

db = client['realty']

tables = db.collection_names();

apartments = db['apartments'];

# apartment = client['realty']['Apartment']

sujis = list(apartments.find({
    'apartment': '창신쌍용2',
    'address_2': '종로구',
    'exclusiveArea': 115.53
    # 'address_3': '성복리'
}).limit(1000).sort('dealedAt', 1))

def del_id(obj):
    del obj['_id']
    del obj['__v']

    return obj

sujis = list(map(del_id, sujis))

x = list(o['dealedAt'] for o in sujis)
y = list(o['price'] for o in sujis)

plt.plot(x, y)

# for item in sujis:
#     pprint(item)
# %%

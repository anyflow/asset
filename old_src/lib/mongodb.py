from pymongo import MongoClient

__DB_NAME_REALTY = 'realty'

__client = MongoClient('mongodb://localhost')

DB_NAMES = __client.list_database_names()
REALTY_DB_TABLES = __client[__DB_NAME_REALTY].list_collection_names()
APARTMENTS = __client[__DB_NAME_REALTY][REALTY_DB_TABLES[0]]

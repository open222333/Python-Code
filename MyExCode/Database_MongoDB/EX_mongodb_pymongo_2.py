from pymongo import MongoClient
from configparser import ConfigParser

# configparser
config = ConfigParser()
config.read('MyExCode/Database_MongoDB/test_config.ini')  # config.example.ini
HOST = config.get('MONGO', 'HOST', fallback='mongodb://localhost:31117/')
DB = config.get('MONGO', 'DB')
COLLECTION = config.get('MONGO', 'COLLECTION')

# pymongo
client = MongoClient(host='mongodb://localhost:31117/')
col = client[DB][COLLECTION]


data = col.find_one()


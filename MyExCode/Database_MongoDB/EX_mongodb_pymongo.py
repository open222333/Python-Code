from pymongo import MongoClient
from datetime import datetime
'''pymongo 基本操作'''

host = '127.0.0.1:31117'  # mongodb預設port
client = MongoClient(host)
db = client['test_db']['test_collection']



# 新增 insert
data = {
    "id": 0,
    "name": "test1",
    "createTime": datetime.now()
}
db.insert(data)

# 新增多筆 用串列
datas = [{
    'id': i,
    'name': f"test{i}",
    "createTime": datetime.now()
} for i in range(1, 10)]

db.insert_many(datas)

# query查詢 EX_mongodb_pymongo_aggregate.py
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

myquery = {"alexa": "10000"}
newvalues = {"$set": {"alexa": "12345"}}

mycol.update_one(myquery, newvalues)


myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

myquery = {"name": {"$regex": "^F"}}
newvalues = {"$set": {"alexa": "123"}}

x = mycol.update_many(myquery, newvalues)

# update 更新
db.test_db.update_many()

# delete 刪除
db.test_db.delete_many()

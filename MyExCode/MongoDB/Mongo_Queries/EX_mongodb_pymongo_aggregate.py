from pymongo import MongoClient
'''pymongo aggregate find 基本操作'''

# 連線到mongodb
client = MongoClient('127.0.0.1:31117')
# db, collection
datas = client['database']['collection']


# find 用法
print(datas.count())  # 有幾筆資料
cursor_datas = datas.find().sort("id", 1).limit(1000).skip(110000)
cursor_datas = datas.find()[100:189]
cursor_datas = datas.find_one({'_id': datas['data']['_id']})
need_datas = [data for data in cursor_datas]

# aggregate 用法
# https://docs.mongodb.com/manual/reference/operator/aggregation/
# pipeline 查詢語法

# dateFromString 用法
# { $dateFromString: {
#      dateString: <dateStringExpression>,
#      format: <formatStringExpression>,
#      timezone: <tzExpression>,
#      onError: <onErrorExpression>,
#      onNull: <onNullExpression>
# } }

# flask mongoengine 用法 - 找重複
# Model._get_collection().aggregate([
#     { '$group' :
#         { '_id' : { 'carrier' : '$carrierA', 'category' : '$category' },
#           'count' : { '$sum' : 1 }
#         }
#     }
# ])

pipeline = [
    {'$group':
        {'_id': {'carrier': '$carrierA', 'category': '$category'},
         'count': {'$sum': 1}
         }
     }
]

cursor_datas = datas.aggregate(pipeline)
print(len([i for i in cursor_datas]))
print([i for i in cursor_datas])

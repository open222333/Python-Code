from pymongo import MongoClient
'''pymongo aggregate find 基本操作'''

host = '127.0.0.1:31117'


def mongo_check_repeat_data(host, db, collection, columns) -> list:
    '''
    查找重複資料 回傳串列
    host:主機:port
    db: 資料庫
    collection: 集合
    columns: 欄位
    db.collection
        .aggregate()
        .group({ _id: '$key', count: { $sum: 1 } })
        .match({ count: { $gt: 1 } })
    '''
    client = MongoClient(host)
    col = client[db][collection]

    pipeline = [
        {'$group': {'_id': f'${columns}', 'count': {'$sum': 1}}},
        {'$match': {'count': {'$gt': 1}}},
    ]

    datas = col.aggregate(pipeline)
    return list(datas)
        

# # 連線到mongodb
# client = MongoClient(host)
# # db, collection
# datas = client['database']['collection']


# # find 用法
# print(datas.count())  # 有幾筆資料
# cursor_datas = datas.find().sort("id", 1).limit(1000).skip(110000)
# cursor_datas = datas.find()[100:189]
# cursor_datas = datas.find_one({'_id': datas['data']['_id']})
# need_datas = [data for data in cursor_datas]

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

# pipeline = [
#     {'$group':
#         {'av_id': {'carrier': '$carrierA', 'category': '$category'},
#          'count': {'$sum': 1}
#          }
#      }
# ]

# cursor_datas = datas.aggregate(pipeline)
# print(len([i for i in cursor_datas]))
# print([i for i in cursor_datas])

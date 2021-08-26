import datetime
from pymongo import MongoClient
from datetime import datetime

# 連線到mongodb
client = MongoClient('127.0.0.1:31117')
# db, collection
datas = client['avnight']['avdata_actor']

# flask mongoengine 用法
# Model._get_collection().aggregate([
#     { '$group' : 
#         { '_id' : { 'carrier' : '$carrierA', 'category' : '$category' }, 
#           'count' : { '$sum' : 1 }
#         }
#     }
# ])

# find 用法
# print(datas.count()) # 有幾筆資料
# cursor_datas = datas.find().sort("av_id", 1).limit(1000).skip(110000)
# cursor_datas = datas.find()[100:189]
# need_datas = [data for data in cursor_datas]

# aggregate 用法
# https://docs.mongodb.com/manual/reference/operator/aggregation/
# pipeline 查詢語法
# db.avdata_video.aggregate([
#     {
#         $addFields:{days:{$divide:[{$subtract: ["$avdata_updated_at","$avdata_created_at"]}, 60 * 60 * 24 * 1000]}}
#     },
#     {
#         $match:{$or:[{days:{$lte:30}}, {avdata_created_at:{$gte:ISODate("2021-07-25T00:00:00.000+08:00")}}]}
#     }
# ]).count();

# dateFromString 用法
# { $dateFromString: {
#      dateString: <dateStringExpression>,
#      format: <formatStringExpression>,
#      timezone: <tzExpression>,
#      onError: <onErrorExpression>,
#      onNull: <onNullExpression>
# } }
# db.getCollection('articles').aggregate([
#     {"$match": {
#         "$expr": {
#             "$and": [
#                 {
#                     "$gte": [
#                         {"$dateFromString": {
#                             "creationDate": "10-08-2018", "format": "%m-%d-%Y"}}
#                     ]
#                 },
#                 {
#                     "$lte": [
#                         {"$dateFromString": {
#                             "creationDate": "10-08-2018", "format": "%m-%d-%Y"}}
#                     ]
#                 }
#             ]
#         }
#     }}
# ])


# 使用日期數學返回 BSON 日期：
# db.test.aggregate([
#     { "$group": {
#         "_id": {
#             "$add": [
#                { "$subtract": [
#                    { "$subtract": [ "$date", datetime.datetime.utcfromtimestamp(0) ] },
#                    { "$mod": [
#                        { "$subtract": [ "$date", datetime.datetime.utcfromtimestamp(0) ] },
#                        1000 * 60 * 60 * 24
#                    ]}
#                ]},
#                datetime.datetime.utcfromtimestamp(0)
#            ]
#         },
#         "count": { "$sum": 1 }
#     }},
#     { "$sort": { "_id": 1 } }
# ])


pipeline = [
    {
        "$addFields": {
                "created_updated_days_divide": {"$divide": [{"$subtract": [{"$dateFromString": {"dateString": "$avdata_updated_at"}}, {"$dateFromString": {"dateString": "$avdata_created_at"}}]}, 60 * 60 * 24 * 1000]},
                "now_updated_days_divide": {"$divide": [{"$subtract": [ datetime.now(), {"$dateFromString": {"dateString": "$avdata_updated_at"}}]}, 60 * 60 * 24 * 1000]}}
    },
    {
        "$match": {"$or":[{"created_updated_days_divide": {"$lte": 30}}, {"now_updated_days_divide": {"$lte": 30}}]}
    }
    # {
    #     "$limit": 1
    # }
]
# cursor_datas = datas.aggregate(pipeline)
# print(len([i for i in cursor_datas]))
# print([i for i in cursor_datas])

# ans = []
# for da in need_datas:
#     for item in [i for i in da]:
#         if item not in ans:
#             ans.append(item)
# print(ans)

# 欄位空直檢查
# maybe_null_col_list = ['birth', 'height', 'cup', 'bust', 'waist', 'hip']
# for col_name in maybe_null_col_list:
#     if col_name not in test_data:
#         test_data[col_name] = None

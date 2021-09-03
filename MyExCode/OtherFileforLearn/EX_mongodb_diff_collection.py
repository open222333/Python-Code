from bson.objectid import ObjectId
from pymongo import MongoClient
'''比對兩份資料 新增沒有的'''
# 連線到mongodb
client = MongoClient('127.0.0.1:31117')
# db, collection
datas_avdata_videos = client['test']['avdata_videos']
datas_temp_upload_tencent = client['test']['temp_upload_tencent']

cursor_avdata_videos = datas_avdata_videos.find()
cursor_temp_upload_tencent = datas_temp_upload_tencent.find().sort('_id', -1)

total_count = abs(cursor_avdata_videos.count() -
                  cursor_temp_upload_tencent.count())
print(total_count)

count = 0
for data in cursor_temp_upload_tencent:
    print(data['data']['code'])
    cursor_avdata_video = datas_avdata_videos.find_one(
        {'_id': data['data']['_id']})
    if cursor_avdata_video == None:
        temp_data = {
            '_id': data['data']['_id'],
            'code': data['data']['code'],
            'origin': data['data']['origin'],
            'videos': data['data']['videos'],
            'direction': data['data']['direction'],
            'genres': data['data']['genres'],
            'languages': data['data']['languages'],
            'creation_date': data['data']['creation_date'],
            'modified_date': data['data']['modified_date'],
        }
        try:
            temp_data['cover'] = data['data']['cover']
        except KeyError:
            pass
        try:
            temp_data['thumb'] = data['data']['thumb']
        except KeyError:
            pass

        datas_avdata_videos.insert(temp_data)
        count += 1
        print(f"count:{count}")
    else:
        pass

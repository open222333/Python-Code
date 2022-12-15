# 使用loads()將json格式資料轉成Python的資料
import json

jsonObj = '{"b":80,"a":25,"c":60}'  # json物件
dictObj = json.loads(jsonObj)  # 轉成Python物件
print(dictObj)
print(type(dictObj))

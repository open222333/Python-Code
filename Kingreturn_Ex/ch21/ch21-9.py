# 讀取login.json的資料
import json

fn = 'ch21/login.json'
with open(fn) as fnObj:
    login = json.load(fnObj)
    print("%s! 歡迎使用本系統！" % login)

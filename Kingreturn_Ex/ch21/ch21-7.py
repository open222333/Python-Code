# 使用load()讀取json檔案
import json

fn = 'ch21/out21_6.json'
with open(fn) as fnObj:
    data = json.load(fnObj)

print(data)
print(type(data))

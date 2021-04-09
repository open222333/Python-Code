# 使用dump()生成json檔案
import json

dictObj = {'b': 80, 'a': 25, 'c': 60}
fn = 'ch21/out21_6.json'
with open(fn, 'w') as fnObj:
    json.dump(dictObj, fnObj)

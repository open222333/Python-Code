# dumps() 的indent參數
import json

dictObj = {'b': 80, 'a': 25, 'c': 60}  # 字典
jsonObj = json.dumps(dictObj, sort_keys=True, indent=4)  # 用內縮呈現json物件
print(jsonObj)

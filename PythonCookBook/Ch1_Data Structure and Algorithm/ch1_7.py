'''
1.7 維持字典的秩序
問題：
建立一個字典(dictionary)，且在迭代(iterating)或序列化(serializing)時，控制其中項目的次序。
解法：
collection模組的OrderedDict:在迭代時完全保留資料插入順序。
若想精準控制JSON編碼中欄位出現的順序，可先建立一個裝有資料的OrderedDict。
討論：
OrderedDict在內部維護一個雙向鏈結串列(doubly linked list)，依照插入的次序來安排鍵值的次序。
一個OrderedDict的大小超過一個正常字典的兩倍大，因創建了額外的鏈結串列。
'''
from collections import OrderedDict
import json


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

# 若想精準控制JSON編碼中欄位出現的順序，可先建立一個裝有資料的OrderedDict。
print(json.dumps(d))

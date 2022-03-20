# 將資料插入陣列
from array import *

x = array('i', [5, 15, 25, 35, 45])  # 建立無號整數陣列

x.insert(2, 100)
for data in x:
    print(data)

# 將字串轉成日期物件
from datetime import datetime
dateObj = datetime.strptime('2017/1/1', '%Y/%m/%d')
print(dateObj)

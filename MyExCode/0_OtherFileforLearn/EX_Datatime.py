import time
from datetime import datetime

# Python time mktime() 函數執行與gmtime(), localtime()相反的操作，它接收struct_time對像作為參數，返回用秒數來表示時間的浮點數。

# 如果輸入的值不是一個合法的時間，將觸發OverflowError 或ValueError。
# print(time.mktime(datetime.today().timetuple()))

# 格式
now_time = datetime.now()
now_utctime = datetime.utcnow()
# print(f"now_time: {now_time}")
# print(f"now_utctime: {now_utctime}")
# datati = '2021-08-13 17:00:02'

# Python time strptime() 函數根據指定的格式把一個時間字符串解析為時間元組。
# print(datetime.strptime(datati, '%Y-%m-%d %H:%M:%S'))
# print(datetime.now().__format__('%Y-%m-%d %H:%M:%S'))
# print(type(datetime.now().__format__('%Y-%m-%d %H:%M:%S')))
# print(f"time.mktime: {time.mktime(now_time.timetuple())}")
# print(datetime.utctimetuple(now_time))
# print(datetime.utcnow())
# print(datetime.ctime(now_time))
# # 時間戳轉 '%Y-%m-%d %H:%M:%S'
# print(datetime.utcfromtimestamp(time.mktime(now_time.timetuple())))
# print(int(datetime.timestamp(now_time)))
# print((datetime.timestamp(datetime.now())))
# print(now_time)


# date_format = '%Y-%m-%d %H:%M:%S'
# now_time = datetime.now().__format__(date_format)
# time.sleep(10)
# end_time = datetime.now().__format__(date_format)
# print(datetime.strptime(end_time, date_format) -
#       datetime.strptime(now_time, date_format))

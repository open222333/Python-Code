import time
from datetime import date, datetime, timedelta, timezone
'''
datetime 文檔
https://docs.python.org/zh-tw/3/library/datetime.html
'''

# Python time mktime() 函數執行與gmtime(), localtime()相反的操作，它接收struct_time對像作為參數，返回用秒數來表示時間的浮點數。

# 如果輸入的值不是一個合法的時間，將觸發OverflowError 或ValueError。
# print(time.mktime(datetime.today().timetuple()))

# 計算30天
date_30_days_ago = (datetime.utcnow() - timedelta(days=30)).timestamp()
# 格式
now_time = datetime.now()
now_utctime = datetime.utcnow()
print(f"now_time: {now_time}")
print(f"now_utctime: {now_utctime}")
print(f"now_utctime: {now_utctime}")
# print('datetime.strptime(datetime.utcnow(), "%Y-%m-%dT%H:%M:%S+00:00"):',
#       datetime.strptime(str(datetime.utcnow()), "%Y-%m-%dT%H:%M:%S+00:00"))
datati = '2021-08-13 17:00:02'

# Python time strptime() 函數根據指定的格式把一個時間字符串解析為時間元組。
print("datetime.strptim(不帶格式):", datetime.strptime(datati, '%Y-%m-%d %H:%M:%S').timetuple())
print("datetime.strptim:", datetime.strptime(datati, '%Y-%m-%d %H:%M:%S'))
print("datetime.now().__format__:", datetime.now().__format__('%Y-%m-%d %H:%M:%S'))
print("datetime.now().__format__:", datetime.now().__format__('%Y-%m-%d'))
print("type(datetime.now().__format__()):", type(datetime.now().__format__('%Y-%m-%d %H:%M:%S')))
print(f"time.mktime: {time.mktime(now_time.timetuple())}")
print("datetime.utctimetuple:", datetime.utctimetuple(now_time))
print("datetime.utcnow():", datetime.utcnow())
print("datetime.ctime():", datetime.ctime(now_time))
# 時間戳轉 '%Y-%m-%d %H:%M:%S'
print("datetime.utcfromtimestamp(time.mktime(now_time.timetuple())):",
      datetime.utcfromtimestamp(time.mktime(now_time.timetuple())))
print("int(datetime.timestamp(now_time)):", int(datetime.timestamp(now_time)))
print("datetime.timestamp(datetime.now()):", (datetime.timestamp(datetime.now())))
print("now_time:", now_time)
print("isoformat", datetime(2019, 5, 18, 15, 17, tzinfo=timezone(timedelta(hours=8))).isoformat())
print(datetime(2019, 5, 18, 15, 17, tzinfo=timezone(timedelta(hours=8))).isoformat())
print(datetime.now().astimezone(timezone(timedelta(hours=8))).isoformat(timespec='seconds'))

a = datetime.now()
b = timedelta(hours=8)
c = a + b
print(f'a(datetime.now()) + b(timedelta(hours=8)) = {c}')
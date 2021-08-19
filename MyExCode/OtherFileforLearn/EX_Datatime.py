import time
from datetime import datetime

# Python time mktime() 函數執行與gmtime(), localtime()相反的操作，它接收struct_time對像作為參數，返回用秒數來表示時間的浮點數。

# 如果輸入的值不是一個合法的時間，將觸發OverflowError 或ValueError。
print(time.mktime(datetime.today().timetuple()))

# 格式
datati = '2021-08-13 17:00:02'
print(datetime.strptime(datati, '%Y-%m-%d %H:%M:%S'))
print(datetime.now().__format__('%Y-%m-%d %H:%M:%S'))
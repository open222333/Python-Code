# 將日期轉成字串格式
import datetime

timeNow = datetime.datetime.now()
print(timeNow.strftime("%Y/%m/%d %H:%M:%S"))
print(timeNow.strftime("%y-%b-%d %H-%M-%S"))
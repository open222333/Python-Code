# 設計一個執行緒單獨執行工作，程式本身也執行工作
import threading
import time


def wakeUp():
    print("threadObj執行緒開始")
    time.sleep(10)  # threadObj 執行緒休息10秒
    print("女朋友生日")
    print("threadObj執行緒結束")


print("程式階段1")
threadObj = threading.Thread(target=wakeUp)
threadObj.start()  # threadObj執行緒開始工作
time.sleep(1)  # 主執行緒休息1秒
print("程式階段2")

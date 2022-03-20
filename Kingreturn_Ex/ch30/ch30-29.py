# Event:一種執行緒的通信技術，通常有2個執行緒，一個主要設定Event的flag，可以使用set()設定flag。另一個則是等待Event的flag，可以用wait()等待。當收到flag訊號工作完成後，可以使用clear()情除flag()訊號。
import random
import time
import threading


def waiter(event, loop):
    for i in range(loop):
        print('%s 等待flag被設定' % (i + 1))
        event.wait()  # 等待flag
        print('等待完成時間：', time.ctime())
        event.clear()  # 重置flag
        print()


def setter(event, loop):
    for i in range(loop):
        time.sleep(random.randint(2, 5))  # 休息一段時間在工作
        event.set()  # 設定flag


event = threading.Event()  # 建立Event物件
loop = random.randint(3, 6)  # 迴圈次數

w = threading.Thread(target=waiter, args=(event, loop))
w.start()
s = threading.Thread(target=setter, args=(event, loop))
s.start()
w.join()
s.join()
print("工作完成！")

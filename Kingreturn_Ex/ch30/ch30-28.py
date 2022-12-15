# Barrier
import random
import time
import threading


def player():
    name = threading.currentThread().getName()
    time.sleep(random.randint(2, 5))
    print('%s 抵達柵欄時間：%s' % (name, time.ctime()))
    b.wait()


b = threading.Barrier(4)  # 等待的執行緒數量
print('比賽開始...')
for i in range(4):
    t = threading.Thread(target=player)
    t.start()
for i in range(4):  # 等待執行緒結束
    t.join()
print("比賽結束")

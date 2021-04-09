# 使用queue 重新設計 ch30_25.py
import threading
import time
import random
import queue

bufSize = 10
q = queue.Queue(bufSize)  # 建立queue，最多10筆


def producer():  # 生產者狀況
    while True:
        if not q.full():  # 如果queue有空間
            item = random.randint(1, 100)  # 生產產品
            q.put(item)  # 將慘品放入庫存
            print("生產者Putting存入 %2s : queue數量 %s" %
                  (str(item), str(q.qsize())))
            time.sleep(2)  # 休息2秒


def consumer():
    while True:
        if not q.empty():  # 如果queue不是空的
            item = q.get()  # 消費產品
            print("消費者Getting取得 %2s : queue數量 %s " %
                  (str(item), str(q.qsize())))
            time.sleep(2)


p = threading.Thread(name='producer', target=producer)  # 建立procuder執行緒
c = threading.Thread(name='consumer', target=consumer)  # 建立consumer執行緒

p.start()
time.sleep(2)
c.start()
time.sleep(2)

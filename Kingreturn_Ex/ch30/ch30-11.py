# 建立執行緒同時列出執行緒的名稱
import threading
import time


def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')


def manager():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')


m = threading.Thread(target=worker)
w = threading.Thread(target=manager)
m.start()
w.start()

#自行命名執行緒
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


w = threading.Thread(target=worker)
m = threading.Thread(target=manager)
w2 = threading.Thread(name="Manager", target=worker)
w.start()
m.start()
w2.start()

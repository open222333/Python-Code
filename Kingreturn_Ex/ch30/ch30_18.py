# 列出在工作中的執行緒數量和這些執行緒的名稱
import threading
import time


def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(), 'Exiting')


def manager():
    print(threading.currentThread().getName(), 'Staring')
    time.sleep(5)
    print(threading.currentThread().getName(), 'Exiting')


w = threading.Thread(name='worker', target=worker)
w.start()
print('worker start join')
w.join(1.5)  # 等待worker執行緒1.5秒工作完成
print('worker end join')
m = threading.Thread(name='manager', target=manager)
m.start()
print('manager start join')
m.join(1.5)  # 等待manager執行緒1.5秒工作完成
print('manager end join')
print("目前共有%d執行緒在工作" % threading.active_count())
for thread in threading.enumerate():
    print("執行緒名稱：", thread.name)

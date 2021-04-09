# 插入子執行緒，先執行完子執行緒後再處理主執行緒
import threading
import time


def worker():
    print(threading.currentThread().getName(), "Starting")
    time.sleep(3)
    print(threading.currentThread().getName(), "Exiting")


w = threading.Thread(name="worker", target=worker)
w.start()
print('start join')  # worker執行緒工作完成才往下執行
w.join()
print('end join')

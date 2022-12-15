# Daemon執行序
import threading
import time


def daemonFun():  # 定義daemon
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(), 'Exiting')


def non_daemon():  # 定義非Daemon
    print(threading.currentThread().getName(), 'Starting')
    print(threading.currentThread().getName(), 'Exiting')


d = threading.Thread(name='daemon', target=daemonFun)  # 建立Daemon
d.setDaemon(False)  # 設為False
nd = threading.Thread(name='non-daemon')  # 建立非Daemon

d.start()
nd.start()

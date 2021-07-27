import threading
import time
lock = threading.Lock()


def job1():
    for i in range(10):
        print('job1', i)


def job2():
    time.sleep(1)
    for i in range(10):
        print('job2', i)


if __name__ == '__main__':
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

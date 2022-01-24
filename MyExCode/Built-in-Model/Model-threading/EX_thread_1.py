import threading
import time


def get_threading_info():
    '''取得執行緒資訊'''
    print('活動中的執行緒數量:', threading.active_count())
    print('當前正在使用的執行緒:', threading.current_thread())
    print('當前正在使用的執行緒名稱:', threading.current_thread().name)
    print('目前活動中的執行緒資訊:', threading.enumerate())


def get_add_threading_info():
    '''取得正在新增的執行緒資訊'''
    print('新增加的執行緒:', threading.current_thread())
    print('新增加的執行緒名稱:', threading.current_thread().name)
    print('活動中的執行緒數量:', threading.active_count())
    time.sleep(100)


def add_threading_job(t_name):
    t = threading.Thread(
        target=get_add_threading_info,
        name=f'thread_info_{t_name}'
    )
    t.start()


if __name__ == '__main__':
    for i in range(0, 10):
        add_threading_job(i)

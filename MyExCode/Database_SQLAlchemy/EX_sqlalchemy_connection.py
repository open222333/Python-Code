from EX_sqlalchemy import set_sqlalchemy_engine
from config import DBNAME
import time
from threading import Thread, active_count, current_thread, enumerate


def get_threading_info():
    '''取得執行緒資訊'''
    print('活動中的執行緒數量:', active_count())
    print('當前正在使用的執行緒:', current_thread())
    print('當前正在使用的執行緒名稱:', current_thread().name)
    print('目前活動中的執行緒資訊:', enumerate())


def set_sqlalchemy_engine_connect(dbname):
    eng_conn = set_sqlalchemy_engine(dbname).connect()
    time.sleep(1000)
    eng_conn.close()


count = 1
while count < 50:
    t = Thread(
        target=set_sqlalchemy_engine_connect,
        args=[DBNAME]
    )
    t.start()
    print(count)
    count += 1

get_threading_info()
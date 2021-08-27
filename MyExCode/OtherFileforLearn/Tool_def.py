# 自製通用函式

from datetime import datetime
import time


def get_status_code(img_path) -> int:
    '''測試鏈結 回傳http code'''
    import requests
    return requests.get(img_path).status_code


def write_logs(file: str, message: str) -> None:
    '''建立log'''
    import os
    if os.path.exists(file) == False:
        f = open(file, 'w')
        f.close()
    f = open(file, 'a')
    f.write(message + "\n")
    f.close()


def spend_time(start: datetime, end: datetime) -> str:
    seconds = (end - start).seconds % 60
    minutes = ((end - start).seconds // 60) % 60
    hours = (((end - start).seconds // 60) // 60) % 24
    days = (((end - start).seconds // 60) // 60) // 24
    return f"{days}天 {hours}時 {minutes}分 {seconds}秒"


def spend_time_secends(total_secends) -> str:
    seconds = total_secends % 60
    minutes = (total_secends // 60) % 60
    hours = ((total_secends // 60) // 60) % 24
    days = ((total_secends // 60) // 60) // 24
    return f"{days}天 {hours}時 {minutes}分 {seconds}秒"

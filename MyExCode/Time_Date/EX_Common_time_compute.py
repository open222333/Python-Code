from datetime import datetime
from typing import Union


def spend_time(start: datetime, end: datetime) -> str:
    '''回傳時間差'''
    seconds = (end - start).seconds % 60
    minutes = ((end - start).seconds // 60) % 60
    hours = (((end - start).seconds // 60) // 60) % 24
    days = (((end - start).seconds // 60) // 60) // 24
    return f"{days}天 {hours}時 {minutes}分 {seconds}秒"


def get_time_str(total_seconds: Union[int, float]) -> str:
    """依照秒數 回傳中文時間

    Args:
        total_seconds (int): 總秒數

    Returns:
        str: 回傳時間
    """
    msg = ''
    seconds = int(round(total_seconds % 60, 0))
    minutes = int((total_seconds // 60) % 60)
    hours = int(((total_seconds // 60) // 60) % 24)
    days = int(((total_seconds // 60) // 60) // 24)
    if days != 0:
        msg += f"{days}天"
    if hours != 0:
        msg += f"{hours}時"
    if minutes != 0:
        msg += f"{minutes}分"
    if seconds != 0:
        msg += f"{seconds}秒"
    return msg


def compute_time(sec):
    import time
    """"""
    date_format = '%Y-%m-%d %H:%M:%S'
    now_time = datetime.now().__format__(date_format)
    time.sleep(sec)
    end_time = datetime.now().__format__(date_format)
    print(datetime.strptime(end_time, date_format) -
          datetime.strptime(now_time, date_format))


def get_time_point(self, total_seconds: Union[int, float]) -> str:
    """依照秒數 回傳 00:00:00格式

    Args:
        total_secends (int): 總秒數

    Returns:
        str: 回傳時間
    """
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

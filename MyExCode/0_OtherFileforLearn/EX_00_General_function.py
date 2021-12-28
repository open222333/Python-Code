# 小工具
from datetime import datetime


def get_priority_objects(datas: list, priority: dict):
    '''取的優先物件 數字大的優先回傳
    datas:資料
    priority: 優先條件 ex:{1:'a', 2:'b'}
    '''
    result = 0
    for key, value in priority.items():
        if value in datas:
            result = max(result, key)
    if result == 0:
        return None
    return result


def set_filename(filename: str, num):
    '''數字 空位補零'''
    return f'{filename}_{str(num).zfill(3)}'


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
    '''回傳時間差'''
    seconds = (end - start).seconds % 60
    minutes = ((end - start).seconds // 60) % 60
    hours = (((end - start).seconds // 60) // 60) % 24
    days = (((end - start).seconds // 60) // 60) // 24
    return f"{days}天 {hours}時 {minutes}分 {seconds}秒"


def spend_time_secends(total_secends: int) -> str:
    '''依照秒數 回傳時間差'''
    seconds = total_secends % 60
    minutes = (total_secends // 60) % 60
    hours = ((total_secends // 60) // 60) % 24
    days = ((total_secends // 60) // 60) // 24
    return f"{days}天 {hours}時 {minutes}分 {seconds}秒"


def checke_url(url: str):
    '''檢查網址 回傳http code'''
    import requests
    try:
        code = requests.get(url, timeout=1).status_code
        if code == 200:
            return True
        elif code == 404:
            return False
        else:
            return code
    except:
        return None


def download_image(url: str):
    '''下載圖片 未完成'''
    from bs4 import BeautifulSoup
    import requests
    import shutil
    import re
    # stream=True 強制解壓縮
    r = requests.get(url, stream=True, timeout=1)
    soup = BeautifulSoup(r.text, 'lxml')
    page_a = soup.findAll('a')
    img_format = ['jpg', 'jpeg', 'png']
    for a in page_a:
        a['href']
    # file_name = url.split("/")[-1]
    # with open(file_name, "wb") as f:
    #     shutil.copyfileobj(r.raw, f)


def create_file(fileName='file', fileFormat='txt', content='', openMode='w'):
    import os
    num = 1
    file = f'{fileName}_{num}.{fileFormat}'
    while True:
        if os.path.exists(file):
            num += 1
        else:
            break
    with open(file, openMode) as f:
        f.write(content)
        # f.close() # with open 會close()


def unquote_encode(url, unicode='utf-8'):
    from urllib.parse import unquote

    url = unquote(url).encode(unicode)
    return url
    # 演示：
    # >>> from urllib.parse import unquote
    # >>> 'example.com?title=%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%B0'
    # >>> unquote(url)
    # 'example.com?title=правовая+защита'


def get_ip_address():
    '''取的對外IP'''
    import urllib3
    url = "https://showip.net/"
    http = urllib3.PoolManager()
    http.headers['User-Agent'] = 'curl/7.49.1'
    r = http.request('GET', url)
    if r.status == 200:
        return r.data.decode("utf-8")
    else:
        return ""


def creatDirTree(dir_path):
    '''創建路徑所有未存在的資料夾'''
    import os
    os.makedirs(dir_path)


def get_random_num(min_num: int, max_num: int) -> int:
    '''取得隨機整數'''
    from random import randint
    return randint(min_num, max_num)


def get_SI_prefix_num(target: str):
    '''國際單位制接頭詞 SI prefix 轉為數字
    參考https://en.wikipedia.org/wiki/Metric_prefix'''
    import re

    SI_prefix = {
        'K': pow(10, 3),
        'M': pow(10, 6),
        'G': pow(10, 9),
        'T': pow(10, 12),
        'P': pow(10, 15),
        'E': pow(10, 18),
        'Z': pow(10, 21),
        'Y': pow(10, 24)
    }
    try:
        split_str = re.findall(r'(.*)(\D)', target)[0]
        if len(split_str) != 0:
            symbol = split_str[1]
            num = float(split_str[0])

            symbol = str(symbol).upper()
            unit = SI_prefix[symbol]
            return int(round(float(num) * unit, 0))
        return int(target)
    except:
        return target


def set_datas(**datas):
    '''兩個*號'''
    for key, value in datas.items():
        print(key, value)

# 小工具
from datetime import datetime


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
    with open(file_name, "wb") as f:
        shutil.copyfileobj(r.raw, f)


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

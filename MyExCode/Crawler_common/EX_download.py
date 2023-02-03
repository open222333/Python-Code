from bs4 import BeautifulSoup
from pprint import pprint
import os
import re
import sys
import shutil
import traceback
import requests

'''
下載大文件
https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests

斷點續傳
https://www.itread01.com/content/1546369412.html
'''


class ProgressBar():
    '''進度條'''

    def __init__(self, title='Progress', symbol='=', bar_size=50) -> None:
        """

        Args:
            title (str, optional): 名稱. Defaults to 'Progress'.
            symbol (str, optional): 進度條圖案. Defaults to '='.
            bar_size (int, optional): 進度條長度. Defaults to 50.
        """
        self.title = title
        self.symbol = symbol
        self.bar_size = bar_size
        self.done = 0  # 迴圈內 使用

    def __call__(self, total: int, done=1, decimal=1, in_loop=False):
        """進度條

        Args:
            total (int): 總數
            done (int, optional): 已完成. Defaults to 1.
            decimal (int, optional): 每次完成. Defaults to 1.
            in_loop (bool, optional): 是否在迴圈內. Defaults to False.
        """
        if in_loop:
            self.done += done
            if self.done >= total:
                self.done = total
            self.__print_progress_bar(self.done, total, decimal)
            if self.done == total:
                self.__done()
        else:
            count = 0
            while True:
                count += done
                if count >= total:
                    count = total
                self.__print_progress_bar(count, total, decimal)
                if count == total:
                    break
            self.__done()

    def __print_progress_bar(self, done:int, total:int, decimal:int):
        """繪製 進度表

        Args:
            done (int): 完成數
            total (int): 總任務數
            decimal (int): 百分比顯示到後面幾位
        """
        # 計算百分比
        precent = float(round(100 * done / total, decimal))
        done_symbol = int(precent / 100 * self.bar_size)
        left = self.symbol * done_symbol
        right = ' ' * (self.bar_size - done_symbol)
        # 顯示進度條
        bar = f"\r{self.title}:[{left}{right}] {format(precent, f'.{decimal}f')}% {done}/{total}"
        sys.stdout.write(bar)
        sys.stdout.flush()

    def __done(self):
        print()


def download_wget(url, file_name, output_dir=None):
    '''使用 wget模組 下載檔案'''
    pass
    # import wget
    # wget.download(url)


def download_file(url, chunk_size=10240, dir=None):
    '''下載大文件
    dir: 目標資料夾'''
    local_filename = url.split('/')[-1]
    if dir != None:
        os.makedirs(dir)
        local_filename = f"{dir}/{local_filename}"

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    return local_filename


def download_file_progress_bar(url, chunk_size=10240):
    '''下載大文件 進度條
    chunk_size:byte數
    output_dir:輸出資料夾位置
    '''
    bar = ProgressBar()
    local_filename = url.split('/')[-1]

    r = requests.get(url, stream=True, timeout=10)
    total = int(r.headers.get('content-length'))
    r.raise_for_status()  # 丟出異常
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            bar(total, done=len(chunk), mode='b')
            f.write(chunk)
    return local_filename


def download_resume_transfer(url, chunk_size=10240, file_name='test', file_extension='', output_dir=None) -> bool:
    '''下載檔案 斷點續傳 功能
    url:網址
    chunk_size:區塊
    file_name:檔名
    file_extension:副檔名
    output_dir:輸出資料夾
    headers Range 說明
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range
    '''

    # 若有副檔名
    if file_extension != '':
        file_name = f'{file_name}.{file_extension}'

    if output_dir != None:
        os.makedirs(output_dir)
        file_name = f'{output_dir}/{file_name}'

    # 解析已下載的大小
    if os.path.exists(file_name):
        # 如果存在 斷點續傳
        file_size = os.path.getsize(file_name)
        open_file_mode = 'ab'

        # 已是完成下載的檔案
        r_first = requests.get(url)
        if int(r_first.headers.get('content-length')) == file_size:
            return True
    else:
        # 如果不存在 非斷點續傳
        open_file_mode = 'wb'
        file_size = 0

    headers = {'Range': f'bytes={file_size}-'}
    r = requests.get(url, stream=True, timeout=15, headers=headers)
    total = r.headers.get('content-length')

    if r.status_code != 206:
        r.raise_for_status()
        return False

    bar = ProgressBar()
    bar.title = file_name

    with open(file_name, open_file_mode) as f:
        count = 0
        for chunk in r.iter_content(chunk_size=chunk_size):
            if count == 0:
                done = len(chunk) + file_size
            else:
                done = len(chunk)
            bar(int(total) + file_size, done, in_loop=True)
            f.write(chunk)
            count += 1

    return True


def download_file_resume_transfer_and_bar(url, file_path, print_bar=True, chunk_size=10240):
    '''下載檔案 斷點續傳 功能 進度條 功能
    url:網址
    chunk_size:區塊(數字)
    file_path:檔案位置 ex:/Users/4ge0/Desktop/test.mp4
    print_bar:顯示進度條
    '''

    # 解析已下載的大小
    if os.path.exists(file_path):
        # 如果存在 斷點續傳
        file_size = os.path.getsize(file_path)
        open_file_mode = 'ab'

        r_first = requests.get(url)
        # 已是完成下載的檔案
        if int(r_first.headers.get('content-length')) == file_size:
            return True
    else:
        # 如果不存在 非斷點續傳
        open_file_mode = 'wb'
        file_size = 0

    headers = {'Range': f'bytes={file_size}-'}
    r = requests.get(url, stream=True, timeout=15, headers=headers)
    total = r.headers.get('content-length')

    if r.status_code != 206:
        r.raise_for_status()
        return False

    bar = ProgressBar()
    bar.title = os.path.basename(file_path)

    with open(file_path, open_file_mode) as f:
        count = 0
        if print_bar:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if count == 0:
                    done = len(chunk) + file_size
                else:
                    done = len(chunk)
                bar(int(total) + file_size, done, in_loop=True)
                f.write(chunk)
                count += 1
        else:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    return True


def check_file_integrity(local_file_path, romate_file_size: int):
    '''檢查檔案完整性 若本地檔案完整 回傳True
    local_file_path: 本地檔案路徑
    romate_file_size: 遠程檔案大小 單位bytes
    '''
    if os.path.exists(local_file_path):
        if romate_file_size == os.path.getsize(local_file_path):
            return True
        else:
            return False
    else:
        return False


def downloadVideo(url, file_name, output_dir=None, file_format="mp4", proxies=None):
    '''
    下載影片函式
    proxies 格式：
        http_proxy  = "http://10.10.1.10:3128"
        https_proxy = "https://10.10.1.11:1080"
        ftp_proxy   = "ftp://10.10.1.10:3128"

        proxyDict = {
                    "http"  : http_proxy,
                    "https" : https_proxy,
                    "ftp"   : ftp_proxy
                    }
    '''

    if os.path.exists(output_dir) == False:
        os.makedirs(output_dir)

    try:
        video = requests.get(url, proxies=proxies)
        if video.status_code == 200:
            file = f'{output_dir}/{file_name}.{file_format}'
            with open(file, 'wb') as f:
                f.write(video.content)
            return file
        else:
            print(video.status_code)
            return False
    except:
        print(traceback.format_exc())


def downloadImage(url, file_name, file_format='png', output_dir=None):
    '''下載圖片'''

    if os.path.exists(output_dir) == False:
        os.makedirs(output_dir)

    try:
        image = requests.get(url)
        if image.status_code == 200:
            file = f'{output_dir}/{file_name}.{file_format}'
            with open(file, 'wb') as i:
                i.write(image.content)
            return file
        else:
            print(image.status_code)
            return False
    except:
        print(traceback.format_exc())


def downloadVideo_ProgressBar(url, file_name, output_dir=None, file_format="mp4", proxies=None):
    '''
    下載影片函式

    進度條
    https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads
    '''

    if os.path.exists(output_dir) == False:
        os.makedirs(output_dir)

    try:
        response = requests.get(url, stream=True, proxies=proxies)
        if response.status_code == 200:
            file = f'{output_dir}/{file_name}.{file_format}'
            with open(file, 'wb') as f:
                total_length = response.headers.get('content-length')

                data_length = 0
                total_length = int(total_length)
                for chunk in response.iter_content(chunk_size=4096):
                    data_length += len(chunk)
                    f.write(chunk)
                    done = int(50 * data_length / total_length)
                    left_s = '=' * done
                    right_s = ' ' * (50 - done)
                    percent = round(100 * data_length / total_length, 1)
                    # 顯示進度條
                    sys.stdout.write(f"\r[{left_s}{right_s}] {percent}%")
                    sys.stdout.flush()
                print()
            return file
        else:
            print(response.status_code)
            return False
    except:
        print(traceback.format_exc())


def get_img_list(urls, class_id=None):
    '''取得圖片列表'''

    def download_img(url, index, ouput_dir):
        '''下載 圖片'''
        if not os.path.exists(ouput_dir):
            os.makedirs(ouput_dir)

        data = requests.get(url)
        with open(f'{ouput_dir}\{str(index).zfill(3)}.jpg', 'wb') as f:
            f.write(data.content)

        return

    img_lists = []
    for url in urls:
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'lxml')

        if class_id != None:
            imgs = soup.find_all('img', f'{class_id}')
        else:
            imgs = soup.find_all('img')

        for img in imgs:
            img_lists.append(img['src'])

    for index in range(0, len(img_lists)):
        download_img(str(img_lists[index]), index + 1, 'D:\code\imgs')


def img_download(url):
    # stream=True 強制解壓縮
    r = requests.get(url, stream=True, timeout=1)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as f:
        shutil.copyfileobj(r.raw, f)


def download_ts(ts_urls, dir_path=None, **headers):
    '''下載ts檔'''
    try:
        for ts_url in ts_urls:
            match = re.split(r'/', ts_url)
            ts_name = match[len(match) - 1]
            if dir_path != None:
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                ts_file = f'{dir_path}/{ts_name}'
            else:
                ts_file = ts_name
            ts_content = requests.get(url=ts_url, headers=headers, stream=True)
            with open(ts_file, 'ab+') as f:
                for chunk in ts_content.iter_content(chunk_size=1024):
                    f.write(chunk)
    except:
        traceback.print_exc()


def merge_ts(ts_dir, ts_name):
    '''合併ts'''
    try:
        all_ts = os.listdir(ts_dir)
        all_ts.sort()
        pprint(all_ts)
        for ts in all_ts:
            _, extension = os.path.splitext(f'{ts_dir}/{ts}')  # 路徑 以及副檔名
            if extension == '.ts':
                with open(f'{ts_dir}/{ts_name}.ts', 'ab+') as f:
                    f.write(open(f'{ts_dir}/{ts}', 'rb').read())
    except:
        traceback.print_exc()


def download_and_merge_ts(ts_urls, dir_path, ts_merge_name=None, **headers):
    '''下載並合併ts檔'''
    try:
        for ts_url in ts_urls:
            match = re.split(r'/', ts_url)
            ts_name = match[len(match) - 1]
            print(f'{ts_name} 下載中...')

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            if ts_merge_name == None:
                ts_merge_name = os.path.dirname(dir_path)

            ts_file = f'{dir_path}/{ts_merge_name}.ts'

            ts_content = requests.get(url=ts_url, headers=headers, stream=True)
            with open(ts_file, 'ab') as f:
                for chunk in ts_content.iter_content(chunk_size=1024):
                    f.write(chunk)
            print(f'{ts_name} 完成')
    except:
        print(f'{ts_name} 異常')
        traceback.print_exc()


def covert_to_to_mp4(ts_path):
    '''轉換ts檔 成 mp4'''
    mp4_file = os.path.basename(ts_path)
    path, _ = os.path.splitext(ts_path)
    command = f'ffmpeg -i {ts_path} {path}.mp4'
    os.system(command)


def get_file_name_from_url(url):
    '''從網址取得檔名'''
    match = re.split(r'/', url)
    file_name = match[len(match) - 1]
    return file_name


# 20230203
def download_file(url: str, file_path: str, print_bar=False, chunk_size=1024000):
    """斷點續傳下載檔案

    Args:
        url (str): 網址
        file_path (str): 檔案位置
        print_bar (bool, optional): 顯示進度條. Defaults to False.
        chunk_size (int, optional): 下載chunk大小. Defaults to 1024000.

    Returns:
        bool: 是否下載成功
    """
    # 解析已下載的大小
    if os.path.exists(file_path):
        # 如果存在 斷點續傳
        try:
            file_size = os.path.getsize(file_path)
            open_file_mode = 'ab'
            r_first = requests.get(url)
            remote_file_size = int(r_first.headers.get('content-length'))
            if remote_file_size < file_size:
                # 檔案大小異常 重載
                os.remove(file_path)
                open_file_mode = 'wb'
                file_size = 0
            elif remote_file_size == file_size:
                # 已是完成下載的檔案
                return True
            bpct = True  # 斷點續傳
        except:
            os.remove(file_path)
            return False
    else:
        # 如果不存在 非斷點續傳
        open_file_mode = 'wb'
        file_size = 0
        bpct = False  # 非斷點續傳

    if bpct:
        headers = {'Range': f'bytes={file_size}-'}
        r = requests.get(url, stream=True, timeout=15, headers=headers)
        total = r.headers.get('content-length')
        if r.status_code != 206:
            print(f"不支援斷點下載 刪除後重載:{file_path} code:{r.status_code}")
            os.remove(os.path.dirname(file_path))
            r.raise_for_status()
            return False

        if r.status_code == 404:
            print(f'code 404 url:{url}')
    else:
        r = requests.get(url, stream=True, timeout=15)
        total = r.headers.get('content-length')
        print(f'非斷點續傳 code:{r.status_code}')

        if r.status_code == 404:
            print(f'code 404 url:{url}')

    bar = ProgressBar()
    bar.title = os.path.basename(file_path)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
        open_file_mode = 'wb'

    with open(file_path, open_file_mode) as f:
        count = 0
        if print_bar:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if count == 0:
                    done = len(chunk) + file_size
                else:
                    done = len(chunk)
                bar(int(total) + file_size, done, in_loop=True)
                f.write(chunk)
                count += 1
        else:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    return True

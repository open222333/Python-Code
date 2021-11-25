import os
import sys
import traceback
import requests
'''
下載大文件
https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests

斷點續傳
https://www.itread01.com/content/1546369412.html
'''


class ProgressBar():
    '''自己設計的進度條'''

    def __init__(self, title='Progress', symbol='=', bar_size=50) -> None:
        '''進度表屬性'''
        self.title = title
        self.symbol = symbol
        self.bar_size = bar_size
        self.done = 0  # 迴圈內 使用

    def __call__(self, total: int, done=1, decimal=1, in_loop=False):
        '''
        in_loop: 建立的實體是否在迴圈內使用
        '''
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

    def __print_progress_bar(self, done, total, decimal):
        '''
        繪製 進度表
        done:完成數
        total:總任務數
        decimal: 百分比顯示到後面幾位
        '''
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


def download_file(url, chunk_size=10240):
    '''下載大文件'''
    local_filename = url.split('/')[-1]
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


url = 'https://www.pexels.com/zh-tw/video/3196600/download/?search_query=%E6%B8%AC%E8%A9%A6&tracking_id=01t32lpgsyg4'
# download_file_progress_bar(url)
download_resume_transfer(url, chunk_size=4096, file_extension='mp4')

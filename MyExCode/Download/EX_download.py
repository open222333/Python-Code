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
    def __init__(self, title='Progress', symbol='=', bar_size=50) -> None:
        '''進度表屬性'''
        self.title = title
        self.symbol = symbol
        self.bar_size = bar_size

        # mode b 使用
        self.done = 0

    def __call__(self, total: int, done=1, decimal=1, mode='a'):
        '''
        mode: 
            a: 建立的實體不在迴圈內使用
            b: 建立的實體在迴圈內使用
        '''
        if mode == 'a':
            count = 0
            while True:
                count += done
                if count >= total:
                    count = total
                self.__print_progress_bar(count, total, decimal)
                if count == total:
                    break
            self.__done()
        elif mode == 'b':
            self.done += done
            if self.done >= total:
                self.done = total
            self.__print_progress_bar(self.done, total, decimal)
            if self.done == total:
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
        '''進度條100%後 進行'''
        print()  # 跳行


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


def download_resume_transfer(url, chunk_size=10240, file_name='test', file_extension='', output_dir=None):
    '''下載檔案 斷點續傳 功能
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
    else:
        # 如果不存在 非斷點續傳
        open_file_mode = 'wb'
        file_size = 0

    headers = {'Range': f'bytes={file_size}-'}
    r = requests.get(url, stream=True, timeout=15, headers=headers)
    if r.status_code != 206:
        r.raise_for_status()
        return
    total = r.headers.get('content-length')

    # 已是完成下載的檔案
    if int(total) == file_size:
        return

    bar = ProgressBar()

    with open(file_name, open_file_mode) as f:
        count = 0
        for chunk in r.iter_content(chunk_size=chunk_size):
            if count == 0:
                done = len(chunk) + file_size
            else:
                done = len(chunk)
            bar(int(total) + file_size, done, mode='b')
            f.write(chunk)
            count += 1
    print(file_name)


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

'''
下載大文件
https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
'''


import sys
import requests


class ProgressBar():
    def __init__(self, title, symbol='=', bar_size=50) -> None:
        self.title = title
        self.symbol = symbol
        self.bar_size = bar_size

    def __call__(self, done, total):
        while True:
            done += done
            self.__print_progress_bar(done, total)
            if done == total:
                break
        print()

    def __print_progress_bar(self, done, total):
        left = self.symbol * done
        right = ' ' * (self.bar_size - done)
        precent = round(100 * done / total, 2)
        sys.stdout.write(f"\r{self.title}:[{left}{right}] {precent}% {done}/{total}")
        sys.stdout.flush()


def downloadVideo_wget(url, file_name, output_dir=None):
    pass
    # import wget
    # wget.download(url)


def download_file(url):
    '''下載大文件'''
    import requests
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


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
    import os
    import requests
    import traceback

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
    import os
    import requests
    import traceback

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
    import os
    import requests
    import traceback

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


# url = 'https://www.pexels.com/zh-tw/video/3196600/download/?search_query=%E6%B8%AC%E8%A9%A6&tracking_id=01t32lpgsyg4'

# downloadVideo_ProgressBar(url, 'test', output_dir='/Users/4ge0/Desktop/test')


url = 'https://video-hw.xvideos-cdn.com/videos/mp4/d/7/a/xvideos.com_d7ac3d8589f8e6a42e9098668fd12831.mp4?e=1636622451&ri=1024&rs=85&h=e5a10b75f60db552208aba06924b40bd'
requests.get(url)

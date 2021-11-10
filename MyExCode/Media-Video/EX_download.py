'''
下載大文件
https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
'''


import sys
import requests


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


def downloadVideo(url, file_name, output_dir=None, file_format="mp4"):
    '''
    下載影片函式
    '''
    import os
    import requests
    import traceback

    if os.path.exists(output_dir) == False:
        os.makedirs(output_dir)

    try:
        video = requests.get(url)
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


def downloadVideo_ProgressBar(url, file_name, output_dir=None, file_format="mp4"):
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
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file = f'{output_dir}/{file_name}.{file_format}'
            with open(file, 'wb') as f:
                total_length = response.headers.get('content-length')

                dl = 0
                total_length = int(total_length)
                for chunk in response.iter_content(chunk_size=4096):
                    dl += len(chunk)
                    f.write(chunk)
                    done = int(50 * dl / total_length)
                    left_s = '=' * done
                    right_s = ' ' * (50 - done)
                    # 顯示進度條
                    sys.stdout.write(f"\r[{left_s}{right_s}] {round(100 * dl / total_length, 1)}%")
                    sys.stdout.flush()
            return file
        else:
            print(response.status_code)
            return False
    except:
        print(traceback.format_exc())


url = 'https://www.pexels.com/zh-tw/video/3196600/download/?search_query=%E6%B8%AC%E8%A9%A6&tracking_id=01t32lpgsyg4'

downloadVideo_ProgressBar(url, 'test', output_dir='/Users/4ge0/Desktop/test')

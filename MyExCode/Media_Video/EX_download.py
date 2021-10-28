'''
下載大文件
https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
'''


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


url = ''
downloadVideo(url, 'test', output_dir='/Users/4ge0/Desktop/test')

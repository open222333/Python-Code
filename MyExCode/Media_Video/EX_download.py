'''
下載大文件
https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
'''
def downloadVideo_wget(url, file_name, output_dir=None):
    pass
    # import wget
    # wget.download(url)


def downloadVideo(url, file_name, output_dir=None, file_format="mp4"):
    '''
    下載影片函式
    '''
    import os
    import requests

    if os.path.exists(output_dir) == False:
        os.makedirs(output_dir)

    try:
        video = requests.get(url).content
        file = f'{output_dir}/{file_name}.{file_format}'
        with open(file, 'wb') as f:
            f.write(video)
        return file
    except Exception as err:
        return err


def downloadImage(url, file_name, file_format='png', output_dir=None):
    import os
    import requests

    if os.path.exists(output_dir) == False:
        os.makedirs(output_dir)

    try:
        image = requests.get(url).content
        file = f'{output_dir}/{file_name}.{file_format}'
        with open(file, 'wb') as i:
            i.write(image)
        return file
    except Exception as err:
        return err


url = 'https://video-hw.xvideos-cdn.com/videos/3gp/4/c/1/xvideos.com_4c12e57a47aa206474a0440f766d6b18.mp4?e=1635154157&ri=1024&rs=85&h=405c773f967ebec486e715d0c252c13e'
downloadVideo(url, 'test', output_dir='/Users/4ge0/Desktop/test')

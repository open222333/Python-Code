def downloadVideo(url, file_name, output_dir=None, file_format="mp4"):
    '''
    下載影片函式
    '''
    import os
    import requests
    if output_dir is not None:
        os.chdir(output_dir)
    try:
        video = requests.get(url).content
        with open(f'{file_name}.{file_format}', 'wb') as f:
            f.write(video)
        return 'OK'
    except Exception as err:
        return err


def downloadImage(url, file_name, file_format='png', output_dir=None):
    import os
    import requests
    if output_dir is not None:
        os.chdir(output_dir)

    try:
        image = requests.get(url).content
        with open(f'{file_name}.{file_format}', 'wb') as i:
            i.write(image)
        return 'OK'
    except Exception as err:
        return err

url = ''
downloadImage(url, 'test', output_dir='/Users/4ge0/Desktop/test')

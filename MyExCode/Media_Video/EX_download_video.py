def downloadVideo(video_url, v_name, dir=None, v_format="mp4"):
    '''
    下載影片函式
    '''
    import os
    import requests
    if dir is not None:
        os.chdir(dir)
    try:
        video = requests.get(video_url).content
        with open(f'{v_name}.{v_format}', 'wb') as f:
            f.write(video)
        return 'OK'
    except Exception as err:
        return err

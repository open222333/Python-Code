import re
from pymediainfo import MediaInfo
import pymediainfo
'''
https://pymediainfo.readthedocs.io/en/stable/pymediainfo.html
'''


def getVideoInfo(video_path):
    '''回傳 影片video_tracks'''
    tracks = MediaInfo.parse(video_path).video_tracks
    return [info.to_data() for info in tracks][0]


def getVideoAspectRatio(video_path):
    '''
    取得影片 長寬比
    '''
    try:
        media = MediaInfo.parse(video_path)
        width = 0
        height = 0
        for track in media.video_tracks:
            width = track.width
            height = track.height
            break
        # 取得小數第二位
        return round(width / height, 2)
    except:
        return 0


def getVideoDuration(video_path):
    '''
    獲取影片 時長
    '''
    import os
    # 取得影片時長資訊
    try:
        duration = 0
        media = MediaInfo.parse(video_path)
        for track in media.video_tracks:
            duration = track.duration
            break
    except:
        pass

    # 使用ffprobe工具
    if duration == 0:
        try:
            command = f'ffprobe -allowed_extensions ALL {video_path} 2>&1 | grep "Duration" | cut -d " " -f 4 | sed s/,//'
            result = os.popen(command).read()
            hour, minute, second = result.split(':')
            duration = ((float(hour) * 3600) + (float(minute)
                        * 60) + int(float(second))) * 1000
        except:
            pass

    return int(duration / 1000)


# 測試用數據
# test_video_path = '/Users/4ge0/Desktop/Pexels_Videos_2278095.mp4'
test_video_path_1 = '/Users/4ge0/Desktop/test_low.mp4'
test_video_path_2 = '/Users/4ge0/Desktop/test_hight.mp4'
test_video_path_3 = '/Users/4ge0/Desktop/test_hight.mp4'
# print(getVideoDuration(test_video_path))
# print(getVideoAspectRatio(test_video_path))
print(getVideoInfo(test_video_path_1)['height'])
print(getVideoInfo(test_video_path_2)['height'])

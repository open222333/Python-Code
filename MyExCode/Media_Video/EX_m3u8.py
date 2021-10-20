import os
import re


def convertVideo_ts(video_path, output_dir, output_name, p):
    '''轉換影片成 ts'''
    from EX_pymediainfo import getVideoInfo
    if os.path.exists(output_dir) == False:
        os.mkdir(output_dir)

    internet_media_type = getVideoInfo(video_path)['internet_media_type']
    internet_media_type = str(re.findall(
        r'H\d{3}', internet_media_type)[0]).lower()
    print(internet_media_type)
    encode = ''

    if internet_media_type == 'h264':
        encode = 'libx264 -crf 23'
    elif internet_media_type == 'h265':
        encode = 'libx265 -crf 28 -tune fastdecode'
    else:
        return ''

    video_name = f'{output_name}-{p}.ts'

    if p == 240:
        command = f'ffmpeg -i {video_path} -c:v {encode} -c:a aac -b:a 192k -r 30 -ar 44100 -video_track_timescale 90000 -vf scale=-2:240 {output_dir}/{video_name} -y'
    elif p == 480:
        command = f'ffmpeg -i {video_path} -c:v {encode} -c:a aac -b:a 192k -r 30 -ar 44100 -video_track_timescale 90000 -vf scale=-2:720 {output_dir}/{video_name} -y'
    else:
        return ''

    print(command)
    os.system(command)
    return video_name


def mergeVideo_m3u8(m3u8_link, video_name, output_dir):
    '''
    合併m3u8
    '''
    name = f'{video_name}.ts'
    command = f'ffmpeg -i {m3u8_link} -c copy {output_dir}/{name} -y'
    os.system(command)
    return name


test_path = '/Users/4ge0/Desktop/test_hight.mp4'
test_dir = '/Users/4ge0/Desktop/test'
# convertVideo_ts(test_path, test_dir, 'test_hight', 480)

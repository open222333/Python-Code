import os
import re
import requests
from datetime import datetime
from pymongo import MongoClient

'''
convertVideo_ts:轉換影片成ts格式
'''


def convertVideo_ts(video_path, output_dir, output_name, p):
    '''
    轉換影片成ts格式
    video_path:影片位置
    output_dir:輸出資料夾位置
    output_name:輸出檔名
    p:畫質
    '''
    from EX_pymediainfo import getVideoInfo
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    internet_media_type = getVideoInfo(video_path)['internet_media_type']
    internet_media_type = str(re.findall(r'H\d{3}', internet_media_type)[0]).lower()
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


def generateKey(out_dir_path, key_name, extension='key', option_hex='16'):
    '''
    使用 openssl 生產 key
    out_dir_path:輸出檔案位置
    key_name:key檔名
    extension:副檔名
    option_hex:位元
    '''
    command = f'openssl rand -hex {option_hex} > {out_dir_path}/{key_name}.{extension}'
    os.system(command)
    return


def generateKeyInfo(key_file_path, filename, key_URI=None, IV=''):
    '''
    key info format(KeyInfo 內容格式):
        key URI        = key_URI
        key file path  = key_file_path
        IV (optional)  = IV

    Key info file example:
        http://server/file.key
        /path/to/file.key
        0123456789ABCDEF0123456789ABCDEF
    '''
    try:
        if key_URI == None:
            key_URI = key_file_path

        data = f'{key_URI}\n{key_file_path}\n{IV}\n'
        with open(f'{filename}.keyinfo', 'w') as f:
            f.write(data)
    except Exception as err:
        return err
    return 'OK'


def mergeVideo_m3u8(m3u8_link, video_name, output_dir):
    '''
    將 m3u8 的影片, 合併成一個 ts 影片, 回傳 ts 檔名稱
    合併m3u8
    '''
    name = f'{video_name}.ts'
    command = f'ffmpeg -i {m3u8_link} -c copy {output_dir}/{name} -y'
    os.system(command)
    return name


def videoTSConvertToEncryptedM3U8(video_ts, keyinfo, output_dir, output_name):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    command = f'ffmpeg -i {video_ts} -c copy -hls_segment_type mpegts -hls_time 1- -start_number 1 -hls_key_info_file {keyinfo} -hls_segment_filename {output_dir}/{output_name}_%05d.ts -hls_list_size 0 -hls_playlist_type vod -hls_flasg delete_segments+split_by_time {output_dir}/{output_name}.m3u8 -y'
    os.system(command)


def is_multimedia(file):
    '''檢測是否正常可播放格式'''
    result = os.system(f'ffprobe {file}')
    if result != 0:
        return False
    else:
        return True


def get_m3u8_ts_list(m3u8_path):
    '''讀取m3u8 取得ts檔'''
    with open(m3u8_path, 'r') as f:
        context = f.readlines()

    result = []
    for i in context:
        if not i.startswith("#"):
            result.append(i.strip())
    return result


def is_m3u(file_name):
    '''是否為m3u檔'''
    target = ['.m3u', '.m3u8']
    ex = os.path.splitext(file_name)[1]
    return ex in target
    
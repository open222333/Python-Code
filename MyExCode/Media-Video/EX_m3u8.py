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


def check_m3u8_url(url):
    command = f'ffprobe {url}'
    result = os.system(command)
    return result


def check_m3u8_local(path):
    command = f'ffprobe {path}'
    result = os.system(command)
    return result


mongo_host = os.environ.get('MONGO_HOST')
mongo_database = os.environ.get('MONGO_DATABASE')
mongo_collection = os.environ.get('MONGO_COLLECTION')

client = MongoClient(mongo_host)
col = client[mongo_database][mongo_collection]


def check_m3u8_urls(s3_bucket, origin: str, max_num: int, min_num=1, qualitys=[240, 480], show_summary=True) -> dict:
    '''判斷已下載並上傳的m3u8內的 #EXT-X-KEY:METHOD=AES-128,URI= 是否正確的值(key_240.key key_480.key)
    回傳:
    result = {
        '240':{
            'successful': list(code),
            'failed': list(code),
            'unknown': list(code),
            'no_exists': list(code),
            'no_download': list(no_download),
        }
        '480':{
            'successful': list(code),
            'failed': list(code),
            'unknown': list(code),
            'no_exists': list(code)
            'no_download': list(no_download),
        }

        summary: {
            '240':{
                'successful': int,
                'failed': int,
                'unknown': int,
                'no_exists': int,
                'no_download': int,
            }
            '480':{
                'successful': int,
                'failed': int,
                'unknown': int,
                'no_exists': int,
                'no_download': int,
            }
        }
    }
    min_num:code的最小編號。預設1。
    max_num:要執行到的code最大編號。
    origin:產品資料夾。
    s3_bucket:AWS的存儲桶CloudFront域名。
    qualitys:畫質。使用list。預設[240, 480]
    show_summary:顯示數據。
    result_file:建立檔案顯示數據。'''
    # #EXT-X-KEY:METHOD=AES-128,URI="key_240.key"
    s = r'#EXT-X-KEY:METHOD=AES-128,URI="(.*?)"'
    result = {}
    summary = {}

    for quality in qualitys:

        successful = []
        failed = []
        unknown = []
        no_exists = []
        no_download = []

        for num in range(min_num, max_num + 1):
            code = f'{origin.upper()}-{str(num).zfill(5)}'
            if get_download_status(code):
                url = f'{s3_bucket}{origin}/{code}/h264/{code}-{str(quality)}.m3u8'
                response = requests.get(url)
                n = os.system(f'ffprobe {url}')
                if response.status_code == 200:
                    res = re.findall(s, response.text)
                    try:
                        if res[0] != f"key_{str(quality)}.key" or n != 0:
                            failed.append(code)
                        else:
                            successful.append(code)
                    except:
                        unknown.append(code)
                else:
                    no_exists.append(code)
            else:
                no_download.append(code)

        result[str(quality)] = {
            'successful': successful,
            'failed': failed,
            'unknown': unknown,
            'no_exists': no_exists,
            'no_download': no_download,
        }
        summary[str(quality)] = {
            'successful': len(successful),
            'failed': len(failed),
            'unknown': len(unknown),
            'no_exists': len(no_exists),
            'no_download': len(no_download),
        }

    os.chdir(os.path.dirname(__file__))
    with open(f"check_m3u8_result_{datetime.now().__format__('%Y-%m-%d')}.txt", 'w') as f:
        f.write(f'總結:\n{summary}\n')
        f.write(f'結果:\n{result}\n')

    if show_summary:
        result['summary'] = summary

    return result


def get_download_status(code) -> bool:
    '''依照code 取得 download status'''
    data = col.find_one({'code': code})
    return data['download']


def set_download_false(code):
    '''依照code 設置 download status 為 false
    以check_m3u8_urls檢查結果 做依據'''

    myquery = {"code": code}
    newvalues = {"$set": {"download": False}}
    col.update_one(myquery, newvalues)

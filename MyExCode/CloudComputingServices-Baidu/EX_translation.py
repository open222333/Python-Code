import random
import hashlib
import urllib
import urllib3
import json
import traceback
from langdetect import detect


def get_language_code(text):
    '''取得 language code'''
    return detect(text)


def translate(q, print_msg=True, source_language_code='auto', target_language_code='zh'):
    '''https://fanyi-api.baidu.com/doc/21 百度翻譯'''
    # 需註冊
    appid = ''
    secretKey = ''

    result = None
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    params = {
        'appid': appid,
        'q': q,
        'from': source_language_code,
        'to': target_language_code,
        'salt': str(salt),
        'sign': sign
    }
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate?' + urllib.parse.urlencode(params)
    print('url = ' + url)
    http = urllib3.PoolManager()
    try:
        r = http.request('GET', url, timeout=3.0)
        if r.status == 200:
            results = json.loads(r.data.decode("utf-8"))
            result = results['trans_result'][0]['dst']
    except:

        traceback.print_exc()
    if print_msg:
        print(f'翻譯目標：\n{q}\n')
        print(f'翻譯結果：\n{result}\n')
    return result


# r = translate('')
# print(r)

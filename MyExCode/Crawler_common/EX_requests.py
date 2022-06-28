import requests
from requests.auth import HTTPProxyAuth
from requests.adapters import HTTPAdapter
import json
from fake_useragent import FakeUserAgent
from base64 import urlsafe_b64encode
import traceback
'''# 20210831
# verify=False 忽略憑證錯誤
user_agent = FakeUserAgent().google  # chrome
proxies = {
    'http': 'http://user:password@proxyip:port',
    'https': 'http://user:password@proxyip:port',
    'ftp': 'http://user:password@proxyip:port'
}

# proxy驗證帳號密碼
username = 'PROXY_USERNAME'
password = 'PROXY_PASSWORD'
auth = f'{username}:{password}'.encode(encoding='ISO-8859-1')
auth = b'Basic ' + urlsafe_b64encode(auth)

url = 'http://quotes.toscrape.com/js/'
response = requests.get(
    url,
    headers={
        'User-Agent': user_agent,
        "Content-Type": "application/json",
        'Proxy-Authorization':  auth
    },
    proxies=proxies,  # 代理伺服器
    params={
        'url': url,
        'wait': 2
    },
    verify=False  # 忽略憑證錯誤
)
'''


class RequestRandomProxy():
    '''設置多個proxy 隨機跳轉'''


    def __init__(self) -> None:
        self.proxies = {}

    def add_proxy(self, host_ip, port, username=None, password=None):
        if username != None and password != None:
            self.proxies[len()]

    def _get_proxy_info(self, proxy):
        response = requests.get('https://ipinfo.io/', proxy)
        ip_info = json.loads(response.text)
        return ip_info


def get_ip(url='https://ipinfo.io/', proxies=None):
    '''
    取得ip - 測試proxy 是否正常
    proxies = {
        'http': 'http://user:password@proxyip:port',
        'https': 'http://user:password@proxyip:port',
        'ftp': 'http://user:password@proxyip:port'
    }
    '''
    try:
        response = requests.get(url, proxies=proxies)
        ip_info = json.loads(response.text)
        return ip_info['ip']
    except:
        traceback.print_exc()


def get_url_retry_ex(url, retry_count=3):
    '''若出錯重試 範例'''
    session = requests.Session()

    # 設定重試次數
    session.mount('http://', HTTPAdapter(max_retries=retry_count))
    session.mount('https://', HTTPAdapter(max_retries=retry_count))

    # RFC 2616中的描述：
    # HTTP/1.1 為發送者定義了“關閉”連接選項，以表明在響應完成後連接將被關閉。例如，
    # Connection: close
    respon = session.get(url, timeout=30, headers={'Connection': 'close'})
    respon_status_code = respon.status_code
    respon.close()
    return respon_status_code

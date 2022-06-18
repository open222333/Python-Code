import requests
from requests.auth import HTTPProxyAuth
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


print(get_ip())
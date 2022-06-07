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


def get_ip(url='https://ipinfo.io/', proxies=None):
    '''
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

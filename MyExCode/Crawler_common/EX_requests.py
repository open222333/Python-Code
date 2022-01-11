import requests
from fake_useragent import FakeUserAgent


# 20210831
# verify=False 忽略憑證錯誤
user_agent = FakeUserAgent().google  # chrome
proxies = {
    'http': 'http://user:password@proxyip:port',
    'https': 'http://user:password@proxyip:port',
    'ftp': 'http://user:password@proxyip:port'
}
url = 'http://quotes.toscrape.com/js/'
response = requests.get(
    url,
    headers={
        'User-Agent': user_agent,
        "Content-Type": "application/json"
    },
    proxies=proxies,  # 代理伺服器
    params={
        'url': url,
        'wait': 2
    },
    verify=False  # 忽略憑證錯誤
)

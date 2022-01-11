'''下載進度條 https://www.itread01.com/articles/1476604849.html

Urlretrieve 的 Python3 寫法
https://oxygentw.net/blog/computer/urlretrieve-python3/
'''
import urllib.request
import requests.packages.urllib3


url = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"
'''
使用 urllib3，就會對 https 的網址出現以下警告：

InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings

通常找到的解決方法是關閉這個警告，如下：

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
'''
requests.packages.urllib3.disable_warnings()


# 不使用open的下載
urllib.request.urlretrieve(url, filename='test')
# urllib.urlretrieve(url, filename="hosts") # python 2 的寫法

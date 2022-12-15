# 網頁伺服器阻擋造成讀取錯誤
import requests

url = 'http://aaa.24ht.com.tw/'
htmlfile = requests.get(url)
htmlfile.raise_for_status()

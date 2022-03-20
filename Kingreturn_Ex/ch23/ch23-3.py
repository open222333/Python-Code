# requests.get() 下載網頁的HTML原始檔案
import requests

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
print(type(htmlfile))

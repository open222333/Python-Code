# 建立Beautifulsoup物件
import requests
import bs4

htmlfile = requests.get('https://deepmind.com.tw/home/')
objSoup = bs4.BeautifulSoup(htmlfile.text, 'html.parser')
#objSoup = BeautifulSoup(htmlfile.text,'lxml')
print("列印BeautifulSoup物件資料型態", type(objSoup))

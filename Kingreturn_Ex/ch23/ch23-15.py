# 去除標籤傳回文字text屬性
import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
print("列印title ＝ ", objSoup.title)
print("title內容 ＝ ", objSoup.title.text)

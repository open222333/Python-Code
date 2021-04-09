# 傳回h1標籤
import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
objTag = objSoup.find('h1')
print('資料型態 ＝ ', type(objTag))
print("列印Tag ＝ ", objTag)
print("Ｔag內容 ＝ ", objTag.text)

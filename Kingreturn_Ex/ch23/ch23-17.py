# 傳回所找尋所有符合的標籤find_all()
import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
objTag = objSoup.find_all('h1')
print('資料型態 ＝ ', type(objTag))
print("列印Tag ＝ ", objTag)
print("以下是列印串列元素：")
for data in objTag:
    print(data.text)

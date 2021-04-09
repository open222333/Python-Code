import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
print("物件類型 ＝ ", type(objSoup.title))
print("列印title ＝ ", objSoup.title)

import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
print("列印BeautifulSoup物件資料型態", type(objSoup))

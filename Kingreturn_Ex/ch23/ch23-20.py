import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
objTag = objSoup.select('p')
print('列出串列元素的資料型態 ＝ ', type(objTag[0]))
print(objTag[0])
print("列出str()轉換過的資料型態 ＝ ", type(str(objTag[0])))
print(str(objTag[0]))

# select()
import bs4
htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
objTag = objSoup.select('p')
print('資料型態 ＝ ', type(objTag))
print("串列長度 ＝ ", len(objTag))
print("元素資料型態 ＝ ", type(objTag[0]))
print("元素內容 ＝ ", objTag[0].getText())

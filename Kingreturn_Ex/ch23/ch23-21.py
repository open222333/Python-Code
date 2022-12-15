#將attrs屬性應用在串列元素 列出字典結果
import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
objTag = objSoup.select('#menu')
print(str(objTag[0].attrs))

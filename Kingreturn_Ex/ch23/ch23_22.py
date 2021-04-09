# 搜尋<p>標籤 列出串列內容與不含子標籤的元素內容
import bs4
htmlFile = open('ch23/index.html',encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile,'html.parser')
objTag = objSoup.select('p')
print("含<p>標籤的串列長度 ＝ ",len(objTag))
for i in range(len(objTag)):
    print(str(objTag[i]))
    print(objTag[i].getText())
    print(objTag[i].text)
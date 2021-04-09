# 標籤字串get()
import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
imgTag = objSoup.select('img')
print("含<img>標籤的串列長度 ＝ ", len(imgTag))
for i in range(len(imgTag)):
    print(imgTag[i])
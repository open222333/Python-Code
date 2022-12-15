# 取得所有圖檔
import bs4

htmlFile = open('ch23/index.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'html.parser')
imgTag = objSoup.select('img')
print("含<img>標籤的串列長度 ＝ ", len(imgTag))
for i in range(len(imgTag)):
    print("列印標籤串列 ＝ ", imgTag[i])
    print("列印圖檔 ＝ ", imgTag[i].get('src'))

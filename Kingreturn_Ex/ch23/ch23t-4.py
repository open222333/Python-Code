import bs4
import requests
import os

from requests.api import head


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
url = 'https://www.pu.edu.tw/'
html = requests.get(url)

destdir = 'ch23/ex23_4'
if os.path.exists(destdir) == False:
    os.mkdir(destdir)

objSoup = bs4.BeautifulSoup(html.text, 'html.parser')
objTag = objSoup.select('img')
print(len(objTag))
if len(objTag) > 0:
    for i in len(objTag):
        imgUrl = objTag[i].get('src')  # 取得圖片的路徑
        finUrl = url + imgUrl

    picture = requests.get(finUrl, headers=headers)
    picture.raise_for_status()

    picFile = open(os.path.join(destdir, os.path.basename(imgUrl)), 'wb')
    for diskStorage in picture.iter_content(10240):
        picFile.write(diskStorage)
    picFile.close()

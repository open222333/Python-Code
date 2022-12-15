# 判斷是否為網址
url = input("請輸入網址：").split('//')
if url[0] == 'http:' or url[0] == 'https:':
    print(url)
else:
    print(url)
    print("此非網址格式")

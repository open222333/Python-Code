# for迴圈應用在資料類別的判斷
names = ['洪錦魁', '洪冰儒', '東霞', '大成']
lastname = []
for name in names:
    if name.startswith('洪'):  # 是否姓氏洪開頭
        lastname.append(name)  # 加入串列
print(lastname)

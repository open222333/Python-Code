# for迴圈應用在資料類別的判斷
files = ['da1.c', 'da2.py', 'da3.py', 'da4.java']
py = []
for file in files:
    if file.endswith('.py'):  # 以.py為副檔名
        py.append(file)  # 加入串列
print(py)

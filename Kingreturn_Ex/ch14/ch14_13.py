# 列出特定工作目錄所有檔案的大小
import os

totalsizes = 0
print('列出ch14工作目錄底下的所有檔案')
for file in os.listdir(os.getcwd() + '/ch14'):
    print(file)
    totalsizes += os.path.getsize(os.path.join(os.getcwd() + '/ch14/', file))

print("全部檔案大小是 ＝ ", totalsizes)

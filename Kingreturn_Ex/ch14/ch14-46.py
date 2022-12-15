# 重新設計ch14_44.py
fn = 'ch14/utf14_45.txt' #設定欲開啟的檔案
file_Obj = open(fn,encoding='utf-8') # 用預設encoding='utf-8'開啟檔案
data = file_Obj.read() #讀取檔案到變數data
file_Obj.close() #關閉檔案物件
print(data)
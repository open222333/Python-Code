# with關鍵字
fn = 'ch14/ch14_15.txt'  # 設定欲開啟的檔案
file_Obj = open(fn)  # 用預設mode=r開啟檔案，傳回檔案物件file_Obj
data = file_Obj.readlines()  # 讀取檔案到變數data
file_Obj.close()  # 關閉檔案物件
msg = ''
for line in data:
    msg += line.rstrip()
print(msg)
# 刪除檔案末端的空白 rstrip()
fn = 'ch14/ch14_15.txt'  # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案，傳為檔案物件file_Obj
    data = file_Obj.read()  # 讀取檔案到變數data
    print(data.rstrip())  # 輸出變數data相當於輸出檔案，同時刪除末端字元

# 分批讀取檔案
fn = 'ch14/ch14_15.txt'  # 設定欲開啟的檔案
chunk = 100
msg = ''
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案，傳回檔案物件file_Obj
    while True:
        txt = file_Obj.read(chunk)  # 一次讀取chunk數量
        if not txt:
            break
        msg += txt
    print(msg)

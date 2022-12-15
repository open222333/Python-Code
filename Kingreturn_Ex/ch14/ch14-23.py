# 字串的替換 replace()
fn = 'ch14/ch14_15.txt'  # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 傳回檔案物件file_Obj
    data = file_Obj.read()  # 讀取檔案到變數data
    new_data = data.replace('test', 'testssss')  # 新變數儲存
    print(new_data.rstrip())  # 輸出檔案

# 逐行讀取使用readlines()
fn = 'ch14/ch14_15.txt'  # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案，傳為檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 一次讀取全部txt，內部是每次讀一行

print(obj_list)  # 列印串列

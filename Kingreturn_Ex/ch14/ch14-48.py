# 使用utf-8-sig
fn = 'ch14/utf14_45.txt'  # 設定欲開啟的檔案
with open(fn, encoding='utf-8-sig') as file_Obj:  # 開啟utf-8檔案
    obj_list = file_Obj.readlines()  # 每次讀一行
print(obj_list)

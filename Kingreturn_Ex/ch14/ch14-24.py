# 數據的搜尋
#
from os import initgroups


fn = 'ch14/ch14_15.txt'  # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案，傳為檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 一次讀取全部txt，內部是每次讀一行

str_Obj = ''  # 先設為空字串
for line in obj_list:  # 將各行字串存入
    str_Obj += line.rstrip()

findstr = input("請輸入欲搜尋的字串 ＝ ")
if findstr in str_Obj:  # 搜尋檔案是否有欲搜尋的字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, fn))
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, fn))

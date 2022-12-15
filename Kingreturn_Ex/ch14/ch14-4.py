# 檢查路徑的方法 exist/isabs/isdir/isfile
import os

print("檔案或資料夾存在 ＝ ", os.path.exists('ch14'))
print("檔案或資料夾存在 ＝ ", os.path.exists('ch14/ch14_3.py'))
print("檔案或資料夾存在 ＝ ", os.path.exists('ch14_4.py'))
print(' --- ')
print("是絕對路徑 ＝ ", os.path.isabs('ch14_4.py'))
print("是絕對路徑 ＝ ", os.path.isabs(
    '/Users/lichengen/Library/Mobile Documents/com~apple~CloudDocs/KingReturnEx/ch14_2.py'))
print(' --- ')
print("是資料夾 ＝ ", os.path.isdir('ch14/ch14_2.py'))
print("是資料夾 ＝ ", os.path.isdir('ch14'))
print(' --- ')
print("是檔案 ＝ ", os.path.isfile('ch14'))
print("是檔案 ＝ ", os.path.isfile('ch14/ch14_2.py'))

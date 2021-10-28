import os
import shutil

# 顯示 環境變數
# print(os.environ)

path = '/Users/4ge0/Desktop/XXXOOPZ-00001'

# 顯示檔案名
# print(os.path.basename(path))

# if os.path.exists(path) == False:
#     # 創建多層次資料夾
#     os.makedirs(path)

# if os.path.exists(path):
#     # 刪除資料夾
#     shutil.rmtree(path)

files = os.listdir(path)
print(files)

import os

# 顯示 環境變數
print(os.environ)

path = '/Users/4ge0/Desktop/uuuuuuuu/test2'
if os.path.exists(path) == False:
    # 創建多層次資料夾
    os.makedirs(path)
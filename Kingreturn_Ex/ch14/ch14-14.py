# 獲得特定工作目錄內容glob
import glob
import os

print("方法1：列出ch14工作目錄的所有檔案")
for file in glob.glob(os.getcwd() + '/ch14/*.*'):
    print(file)

print("方法2：列出目前工作目錄的特定檔案")
for file in glob.glob(os.getcwd() + '/ch14/ch14_1*.py'):
    print(file)

print("方法3：列出目前工作目錄的特定檔案")
for file in glob.glob(os.getcwd() + '/ch14/ch14_2*.*'):
    print(file)

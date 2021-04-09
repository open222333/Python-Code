# 遍歷目錄樹 os.walk()
import os

for dirName, sub_dirNames, fileNames in os.walk(os.getcwd()):
    print('目前工作目錄名稱：', dirName)
    print('目前子目錄名稱串列：', sub_dirNames)
    print('目前檔案名稱串列：', fileNames)

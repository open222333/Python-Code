import os

fileName = input("請輸入要建立的檔案名稱(位置在ch14/train/內)：")
filePath = 'ch14/train/' + fileName
if os.path.exists(filePath):
    print('檔案大小為：', os.path.getsize(filePath))
else:
    print('%s檔案不存在' % fileName)

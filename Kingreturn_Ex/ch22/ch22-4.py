# 使用串列索引讀取csv內容
import csv

fn = 'ch22/population.csv'
with open(fn) as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列

print(listReport[0][1], listReport[0][2])

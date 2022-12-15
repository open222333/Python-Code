# 用迴圈列出Reader物件資料
import csv

fn = 'ch22/population.csv'
with open(fn) as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀檔案建立Reader物件
    for row in csvReader:
        print('Row %s = ' % csvReader.line_num, row)

# 列出標題資料
import csv

fn = 'ch22/population.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)  # 讀取文件下一行
print(headerRow)

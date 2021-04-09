# 輸出串列 writerow()
import csv

fn = 'ch22/out22_7.csv'
with open(fn, 'w',newline='') as csvFile:  # 開啟csv檔案
    csvWriter = csv.writer(csvFile)  # 建立Writer物件
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
import csv

fn = 'ch22/population.csv'
with open(fn) as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀檔案建立Reader物件
    listReport = list(csvFile)  # 將資料轉成串列
for row in listReport:  # 使迴圈列出串列內容
    print(row)

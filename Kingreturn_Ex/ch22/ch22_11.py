# 將欲寫入csv檔案改成串列資料
import csv

dictlist = [{'Name': 'Hung', 'Age': '35', 'City': 'Taipei'},  # 定義串列，元素是字典
            {'Name': 'James', 'Age': '40', 'City': 'Chicago'}]
fn = 'ch22/out22_11.csv'
with open(fn, 'w', newline='') as csvFile:
    fields = ['Name', 'Age', 'City']
dictWriter = csv.DictWriter(csvFile, fieldnames=fields)  # 建立Writer物件

dictWriter.writeheader()  # 寫入標題
for row in dictlist:
    dictWriter.writerow(row)

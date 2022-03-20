# 寫入字典資料DictWriter()
import csv

fn = 'ch22/out22_10.csv'
with open(fn, 'w', newline='') as csvFile:
    fields = ['Name', 'Age', 'City']
    dictWriter = csv.DictWriter(csvFile, fieldnames=fields)

    dictWriter.writeheader()  # 寫入標題
    dictWriter.writerow({'Name': 'Hung', 'Age': '35', 'City': 'Taipei'})
    dictWriter.writerow({'Name': 'James', 'Age': '40', 'City': 'Chicago'})

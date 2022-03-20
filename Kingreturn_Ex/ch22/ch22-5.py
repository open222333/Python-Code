# DictReader()：讀取csv檔案，傳回排序字典(OrderedDict)類型。
import csv

fn = 'ch22/population.csv'
with open(fn) as csvFile:
    csvDictReader = csv.DictReader(csvFile)  # 讀取檔案建立DictReader物件
    for row in csvDictReader:
        print(row)

# 解析出部分內容
import csv

fn = 'ch22/population.csv'
with open(fn) as csvFile:
    csvDictReader = csv.DictReader(csvFile)
    for row in csvDictReader:
        if row['Year'] == '2000':
            print(row['Country Name'], row['Value'])

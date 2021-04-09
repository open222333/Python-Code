# 應用enumerate()
import csv

fn = 'ch22/population.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)

for i, header in enumerate(headerRow):
    print(i, header)

# 複製csv檔案
import csv

infn = 'ch22/population.csv'  # 來源檔案
outfn = 'ch22/out22_8.csv'  # 目的檔案
with open(infn) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)

with open(outfn, 'w', newline='') as csvOFile:
    csvWriter = csv.writer(csvOFile)
    for row in listReport:
        csvWriter.writerow(row)

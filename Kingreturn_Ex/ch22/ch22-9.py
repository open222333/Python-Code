# delimiter關鍵字
import csv

fn = 'ch22/out22_9.csv'
with open(fn, 'w', newline='') as csvFile:
    csvWiter = csv.writer(csvFile, delimiter='\t')
    csvWiter.writerow(['Name', 'Age', 'City'])
    csvWiter.writerow(['Hung', '35', 'Taipei'])
    csvWiter.writerow(['James', '40', 'Chicago'])

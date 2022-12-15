import csv

fn = 'ch22/population.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)
    name, code = [], []
    for row in csvReader:
        if row[2] == '2000':
            name.append(row[0])
            code.append(row[1])

print(name)
print(code)

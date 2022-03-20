import csv
# import matplotlib.pyplot as plt

fn = 'ch22/population.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)
    population = []
    for row in csvReader:
        if row[1] == 'CHI':
            population.append(row[3])

# plt.plot(population)
# plt.title('CHI Population', fontsize=24)
# plt.xlabel("", fontsize=14)
# plt.ylabel("Population", fontsize=24)
# plt.tick_params(axis='both', labelsize=12, color='red')
# plt.show()

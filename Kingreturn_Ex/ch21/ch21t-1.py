import json

fn = 'ch21/population.json'
with open(fn) as fnObj:
    Datas = json.load(fnObj)

for Data in Datas:
    if Data['Year'] == 2000:
        countryName = Data['Country Name']
        countryCode = Data['Country Code']
        population = int(float(Data['Value']))
        print("國家名稱：%s\n國家代碼：%s\n人口數：%d\n" %
              (countryName, countryCode, population))

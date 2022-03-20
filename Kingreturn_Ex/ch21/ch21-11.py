import json

fn = 'ch21/population.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀json檔案
for getData in getDatas:
    if getData['Year'] == 2000:  # 篩選2000年的數據
        countryName = getData['Country Name']  # 國家名稱
        countryCode = getData['Country Code']  # 國家代碼
        population = int(float(getData['Value']))  # 如口數據
        print('國家代碼 ＝', countryCode, '國家名稱 ＝', countryName, '人口數 ＝', population)

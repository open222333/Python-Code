import json
from pygal_maps_world.i18n import COUNTRIES


def getCountryCode(countryName):
    '''輸入國家名稱回傳國家代碼'''
    for dictCode, dictName in COUNTRIES.items():  # 搜尋國家與國家代碼字典
        if dictName == countryName:
            return dictCode  # 如果找到則回傳國家代碼
    return None  # 找不到則回傳None


fn = 'ch21/population.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀取人口數據json檔案

for getData in getDatas:
    if getData['Year'] == 2000:  # 篩選2000年的數據
        countryName = getData['Country Name']  # 國家名稱
        countryCode = getCountryCode(countryName)
        population = int(float(getData['Value']))  # 人口數
        if countryCode != None:
            print(countryCode, ":", population)  # 國家名稱相符
        else:
            print(countryCode, '名稱不相符')  # 國家名稱不相符

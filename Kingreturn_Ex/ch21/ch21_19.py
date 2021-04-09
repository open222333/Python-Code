# 依據一億人進行顏色分類
import json
import pygal_maps_world.maps
from pygal_maps_world.i18n import COUNTRIES


def getCountryCode(countryName):
    '''輸入國家名稱回傳國家代碼'''
    for dictCode, dictName in COUNTRIES.items():  # 搜尋國家與國家代碼
        if dictName == countryName:
            return dictCode  # 如果找到則回傳國家代碼
    return None


fn = 'ch21/population.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)  # 讀取人口數據json檔案


dictData = {}  # 定義地圖使用的字典
for getData in getDatas:
    if getData['Year'] == 2000:  # 篩選2000年的數據
        countryName = getData['Country Name']  # 國家名稱
        countryCode = getCountryCode(countryName)
        population = int(float(getData['Value']))  # 人口數
        if countryCode != None:
            dictData[countryCode] = population  # 代碼：人口數據 加入字典

dict1, dict2 = {}, {}  # 定義人口分級的字典
for code, population in dictData.items():
    if population > 100000000:
        dict1[code] = population  # 人口數大於一億
    else:
        dict2[code] = population  # 人口數小於一億

worldMap = pygal_maps_world.maps.World()
worldMap.title = 'World Population in 2000'
worldMap.add('Over 100000000', dict1)
worldMap.add('Under 100000000', dict2)
worldMap.render_to_file('ch21/out21_19.svg')  # 儲存地圖檔案

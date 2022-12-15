# 繪製世界人口地圖
import json
import pygal_maps_world.maps
from pygal_maps_world.i18n import COUNTRIES


def getCountryCode(countryName):
    '''輸入國家名稱回傳國家代碼'''
    for dictCode, dictName in COUNTRIES.items():  # 搜尋國家與國家代碼字典
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
            dictData[countryCode] = population  # 代碼：人口數據加入字典

worldMap = pygal_maps_world.maps.World()
worldMap.title = 'World Population in 2000'
worldMap.add('Year 2000', dictData)
worldMap.render_to_file('ch21/out21_18.svg')  # 儲存地圖檔案

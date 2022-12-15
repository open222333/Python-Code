import json
import pygal_maps_world.maps as pm
from pygal_maps_world.i18n import COUNTRIES


def getCountryCode(countryName):
    '''依照國家名傳回代碼'''
    for dictCode, dictName in COUNTRIES.items():
        if countryName == dictName:
            return dictCode
    return None


fn = 'ch21/population.json'
with open(fn) as fileobj:
    datas = json.load(fileobj)

dict1, dict2, dict3, dict4, dict5 = {}, {}, {}, {}, {}
for data in datas:
    if data['Year'] == 2000:
        countryName = data['Country Name']
        countryCode = getCountryCode(countryName)
        population = data['Value']
        if countryCode != None:
            if population > 100000000:
                dict1[countryCode] = population
            elif population > 50000000:
                dict2[countryCode] = population
            elif population > 10000000:
                dict3[countryCode] = population
            elif population > 5000000:
                dict4[countryCode] = population
            else:
                dict5[countryCode] = population

worldMap = pm.World()
worldMap.title = '2000年人口'
worldMap.add('1億以上', dict1)
worldMap.add('5000萬以上低於1億', dict2)
worldMap.add('1000萬以上低於5000萬', dict3)
worldMap.add('500萬以上低於1000萬', dict4)
worldMap.add('500萬以下', dict5)
worldMap.render_to_file('ch21/out21t_5.svg')

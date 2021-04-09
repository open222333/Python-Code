from pygal_maps_world.i18n import COUNTRIES

for countryCode in sorted(COUNTRIES.keys()):
    print("國家代碼：", countryCode, "國家名稱＝", COUNTRIES[countryCode])

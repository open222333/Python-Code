# 批量建立字典
armys = []  # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag': 'red', 'score': 3, 'speed': 'slow'}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵的資料")
for soldier in armys[:3]:
    print(soldier)
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    soldier['tag'] = 'blue'
    soldier['score'] = 5
    soldier['speed'] = 'medium'
# 列印編號35到40的小兵
print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)

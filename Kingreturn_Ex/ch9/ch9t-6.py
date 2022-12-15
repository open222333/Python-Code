# 批量建立字典
armys = []  # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag': 'red', 'score': 3, 'speed': 'slow'}
    armys.append(soldier)
# 列印前3個小兵
print("後3名小兵的資料")
for soldier in armys[-3:]:
    soldier['tag'] = 'green'
    soldier['score'] = 10
    soldier['speed'] = 'fast'
print(armys)

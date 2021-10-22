'''
1.20 將多個映射結合為單一映射
問題：
有多個字典(dictionaries)或映射(mappings)，要合理的方式將他們結合，已進行某種動作，例如：值得查找或檢查鍵值是否存在。
解法：
collrctions模組的ChainMap類別。
討論：
ChainMap 若有變動都會變動第一個映射的值。
ChainMap特別適合用於具有範疇的值(scoped values，如全域值、區域值等)
作為ChainMap的替代方案，可以考慮使用update()方法將字典合併合併再一起。
'''
from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
# 先在a找 a沒有再到b找
print(c['z'])

print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']  # 出現錯誤

values = ChainMap()
values['x'] = 1
# 新增一個映射
values = values.new_child()
values['x'] = 2
# 新增一個映射
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])

# 丟棄最後一個映射
values = values.parents
print(values['x'])

# 丟棄最後一個映射
values = values.parents
print(values['x'])

print(values)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)
print(merged['x'])
print(merged['y'])
print(merged['z'])

a['x'] = 13
print(merged['x'])

merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])

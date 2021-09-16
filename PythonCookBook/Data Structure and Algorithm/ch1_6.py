'''
1.6 在一個字典中將鍵值映射至多個值
問題：
製作一個字典，將各個鍵值(keys)映射到一個以上的值(multidict)
解法：
將值使用串列或集合儲存。
串列：保留插入順序
集合：移除重複項目
可使用collections模組中的defaultdict：自動初始化第一個值，可專注在值的新增。會自動建立字典條目(dictionary entries)
若不想要自動建立字典條目，可使用setdefult()
討論：
使程式碼更簡潔
'''
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(4)
print(d2)

d3 = {}
d3.setdefault('a', []).append(1)
d3.setdefault('a', []).append(2)
d3.setdefault('b', []).append(4)

pairs = {1: 'a', 2: 'b'}

d4 = {}
for key, value in pairs:
    if key not in d4:
        d4[key] = []
    d[key].append(value)

d5 = defaultdict(list)
for key, value in pairs:
    d5[key].append(value)

'''
1.9 找出兩個字典的共通處
問題：
找出兩個字典共通的鍵值(keys)、值(values)
解法：
使用keys()或item()做簡單的集合運算(set operations)，這類運算也這類運算也可用來更動或過濾字典的內容。
討論：
一個字典就是一個鍵值(key)集合與一個值(value)集合之間的映射(mapping)。
字典的keys()會回傳一個揭露這些鍵值的keys-view物件。這些物件支援集合運算。
字典的items()會回傳一個items-view物件，由(key, value)對組構成。這些物件支援集合運算。
字典的values()不支援集合運算。原因：values-view 值不保證唯一，使得某些集合運算失去功用。
'''
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 使用keys()或item()做簡單的集合運算(set operations)，這類運算也這類運算也可用來更動或過濾字典的內容。
# 找出共通的鍵值(keys)
print(a.keys() & b.keys())
# 找出在a但不在b的鍵值
print(a.keys() - b.keys())
# 找出共通的對組
print(a.items() & b.items())

# 製作一個特定鍵值被移除的新字典
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)

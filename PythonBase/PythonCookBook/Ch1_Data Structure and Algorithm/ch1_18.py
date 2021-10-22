'''
1.18 將名稱映射至序列元素
問題：
有段程式碼會依據位置存取串列(list)或元組(tuple)的元素，想用名稱存取元素，使結構少依賴位置。
解法：
collection.namedtuple()。
討論：
nametuple：可以用來取代字典，因字典所需儲存空間較大。然而不同於字典的是，nametuple的內容不可變(immutable)。
若需要變更屬性，可通過nametuple實體的_replace()方法，會建立一個全新的nametuple。
_replace()巧妙的用途：填充(populate)，具有選擇性欄位或缺少欄位的具名元組。先製作一個有預設值的原型元組，然後用_replace()建立一個植被取代的新實體。
若是定義一種有效率的資料結構，可以考慮使用__slots__定義一個類別。(訣竅 8.4)
'''
from collections import namedtuple
Subscriber = namedtuple('Subcriber', ['addr', 'joined'])
sub = Subscriber('jones@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

# 具名元組(named tuples) 一個主要用途：讓程式碼可以與操作的元素之位置分離。


def compute_cost(records):
    # 使用普通元組的程式碼
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)
print(s)
# s.shares = 75 # AttributeError: can't set attribute 發生錯誤
s = s._replace(shares=75)
print(s)

# _replace()巧妙的用途：填充(populate)，具有選擇性欄位或缺少欄位的具名元組。先製作一個有預設值的原型元組，然後用_replace()建立一個植被取代的新實體。
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# 建立一個原形實體
stock_prototype = Stock('', 0, 0.0, None, None)

# 用來將字典轉為Stock的函式


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))

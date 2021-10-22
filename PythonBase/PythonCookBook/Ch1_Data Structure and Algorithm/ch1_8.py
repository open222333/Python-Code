'''
1.8 以字典進行運算
問題：
在一個資料字典(dictionary)，進行各種運算。
解法：
使用zip()反轉(invert)這個鍵值的keys與values。
使用zip()搭配sorted()進行排序。
注意：zip()建立一個只能消耗一次的迭代器(iterator)
討論：
若在字典進行常見的資料縮簡(data reductions)，只會處理鍵值(keys)。
zip()反轉成(values,keys)的序列，先比較value，若剛好有一樣的值，會比較鍵值(key)。
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 以下會出錯 注意：zip()建立一個只能消耗一次的迭代器(iterator)
prices_and_names = zip(prices.values(), prices.keys())
print(max(prices_and_names))  # OK
try:
    print(min(prices_and_names))  # ValueError: min() arg is an empty sequence
except Exception as err:
    print(err)

# 若在字典進行常見的資料縮簡(data reductions)，只會處理鍵值(keys)。
min(prices)
max(prices)

min(prices.values())
max(prices.values())

# 可回傳正確資料
min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])

# 取得值須額外處理
min_value = prices[min(prices, key=lambda k:prices[k])]

# zip()反轉成(values,keys)的序列，先比較value，若剛好有一樣的值，會比較鍵值(key)。
prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))

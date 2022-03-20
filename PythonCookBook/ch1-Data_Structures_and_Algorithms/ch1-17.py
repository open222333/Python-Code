'''
## 1.17 擷取出一個字典的子集合

問題：

```
製作一個字典，為另個字典的子集(subset)
```

解法：

```
使用字典概括式(dictionary comprehension)能夠輕易達成目標。
```

討論：

```
建立一個元組序列(a sequen of tuples)並傳給dict函式。也可達成字典概括能做到的大部分事情。

```

'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 找出所有股價大於200的股票做成一個字典
p1 = {key: value for key, value in prices.items() if value > 200}

# 製作一個科技股字典
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}

# 建立一個元組序列(a sequen of tuples)並傳給dict函式。也可達成字典概括能做到的大部分事情。
# 但速度較慢
p3 = dict((key, value) for key, value in prices.items() if value > 200)

p4 = {key: prices[key] for key in prices.keys() if key in tech_names}

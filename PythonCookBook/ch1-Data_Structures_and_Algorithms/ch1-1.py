'''
## 1.1 將一個序列拆分給個別變數

問題：

```
有一個Ｎ個元素的元組(tuple)或序列(sequen),拆分給Ｎ個變數
```

解法：

```
賦值(assignment operation) 拆分給變數
```

討論：

```
拆分(unpacking)可用在任何可迭代物件(iterable)：元組 串列 字串 檔案 迭代器(iterators) 產生器(generators)
用了就丟的變數名稱(throwaway variable name)：_，須確保所挑的名稱沒用在其他地方
```

'''
# 將一個序列拆分給個別變數
p = (4, 5)
x, y = p
print(x)
print(y)


data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)

name, shares, price, (year, mon, day) = data
print(year)
print(mon)
print(day)

# 結論
# 拆分(unpacking)可用在任何可迭代物件(iterable)
# 元組 串列 字串 檔案 迭代器(iterators) 產生器(generators)
s = "hello"
a, b, c, d, e = s
print(a)
print(b)
print(c)

# 拆分時 丟棄某些值
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)

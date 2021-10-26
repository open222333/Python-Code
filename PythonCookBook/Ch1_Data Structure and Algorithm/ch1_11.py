'''
1.11 為一個切片(Slice)命名
問題：
若清理程式充斥著寫死(hardcoded)在程式碼中的切片索引(slice indices)
解法：
程式碼範例
討論：
內建的slice()會建立一個slice物件，可用在任何允許切片(slice)的地方。
假設有個slice實體s，可用s.start、s.stop、s.step取得更多資訊。
可使用indices(size)會回傳(start, stop, step)元組(tuple)。
'''
# 0123456789012345678901234567890123456789012345678901234567890123456789
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)

# 內建的slice()會建立一個slice物件，可用在任何允許切片(slice)的地方。
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

# 可使用indices(size)會回傳(start, stop, step)元組(tuple)。
a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])

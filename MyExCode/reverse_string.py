# 16種反轉字串的方法
# 方法1 反轉串列法
import collections
from functools import reduce
a = 'abcdef'
b = list(a)
b.reverse()
b = ''.join(b)
print(b)

# 方法2 迴圈反向迭代法
a = 'abcdef'
b = ''
for i in a:
    b = i + b
print(b)

# 方法3 反向回圈迭代法
a = 'abcdef'
b = ''
for i in a[::-1]:
    b += i
print(b)

# 方法4 倒序切片法
a = 'abcdef'
b = a[::-1]
print(b)

# 方法5 遍歷索引法
a = 'abcdef'
b = ''
for i in range(1, len(a) + 1):
    b += a[-i]
print(b)

# 方法6 串列彈出法
a = 'abcdef'
a = list(a)
b = ''
while len(a) > 0:
    b += a.pop()
print(b)

# 方法7 串列解析式法
a = 'abcdef'
b = ''.join(i for i in a[::-1])
print(b)

# 方法8 反向遍歷索引法
a = 'abcdef'
b = ''
for i in range(len(a) + 1, 1, 1):
    b += a[i]
print(b)

# 方法9 累積相加法
a = 'abcdef'


def f(x, y):
    return y + x


b = reduce(f, a)
print(b)

# 方法10 匿名函式法
a = 'abcdef'
b = reduce(lambda x, y: y + x, a)
print(b)

# 方法11 串列倒敘法
a = 'abcdef'
a = list(a)
a.sort(reverse=True)
b = ''.join(a)
print(b)

# 方法12 雙向佇列排序法
a = 'abcdef'
b = collections.deque()
for i in a:
    b.appendleft(i)
b = ''.join(b)
print(b)

# 方法13 雙向佇列反轉法
a = 'abcdef'
b = collections.deque()
b.extend(list(a))
b.reverse()
b = ''.join(b)
print(b)

# 方法14 一維陣列索引法
# a = 'abcdef'
# import pandas as pd
# b = pd.Series(list(a))
# b = ''.join(b[::-1])
# print(b)

# 方法15 函式遞迴法
a = 'abcdef'


def f(a):
    if len(a) <= 1:
        return a
    return a[-1] + f(a[:-1])


b = f(a)
print(b)

# 方法16 對稱交換法
a = 'abcdef'


def f(a):
    a = list(a)
    if len(a) <= 1:
        return a
    i = 0
    length = len(a)
    while i != length/2:
        a[i], a[length - 1 - i] = a[length - 1 - i], a[i]
        i += 1
    return ''.join(a)


b = f(a)
print(b)

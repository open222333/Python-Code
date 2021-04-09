# frozenset 凍結集合
x = frozenset([1, 3, 5])
y = frozenset([5, 7, 9])
print(x)
print(y)
print("交集 ＝ ", x & y)
print("聯集 ＝ ", x | y)
a = x & y
print("交集a ＝ ", a)
a = x.intersection(y)
print("交集a ＝ ", a)

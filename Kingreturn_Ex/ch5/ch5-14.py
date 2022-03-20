# 計算聯立線性方程式
a = 2
b = 3
c = 1
d = -2
e = 13
f = -4
x = (e * d - b * f) / (a * d - b * c)
y = (a * f - e * c) / (a * d - b * c)
print("x = %6.4f, y = %6.4f" % (x, y))

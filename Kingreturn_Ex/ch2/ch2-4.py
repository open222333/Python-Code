# 將一個敘述分成多行的應用
a = b = c = 10
x = a + b + c + 12
print(x)
# 續行方法1
y = a +\
    b +\
    c +\
    12
print(y)
# 續行方法2
z = (a + # 此處可加上註解
     b +
     c +
     12 )
print(z)
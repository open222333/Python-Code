# 計算ax^2 + bx + c = 0
a, b, c = eval(input("ax^2 + bx + c = 0,請輸入a,b,c："))
r = b ** 2 - 4 * a * c
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
if r > 0:
    print("兩個實數根：%4.2f,%4.2f" % (r1, r2))
elif r == 0:
    print("兩個實數根：%4.2f" % (r1))
else:
    print("沒有實數根")

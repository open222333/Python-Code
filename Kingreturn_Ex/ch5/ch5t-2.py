# 輸入3個數字 大排到小
x1, x2, x3 = eval(input("請輸入三個數字用逗號隔開："))
if x1 > x2 and x1 > x3:
    if x2 > x3:
        print(x1, x2, x3)
    else:
        print(x1, x3, x2)
elif x2 > x1 and x2 > x3:
    if x1 > x3:
        print(x2, x1, x3)
    else:
        print(x2, x3, x1)
else:
    if x1 > x2:
        print(x3, x1, x2)
    else:
        print(x3, x2, x1)

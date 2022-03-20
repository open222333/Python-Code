# 重新設計ch5_14.py
print("ax + by = e\ncx + dy = f")
a,b,c,d,e,f = eval(input("請輸入a,b,c,d,e,f："))
flog = a * d - b * c
x = (e * d - b * f) / (a * d - b * c)
y = (a * f - e * c) / (a * d - b * c)
if flog == 0:
    print("無解")
else:
    print("x = %6.4f, y = %6.4f" % (x, y))
# 輸入三位數 捨去個位數
num = eval(input("請輸入三位數整數："))
if 99 < num < 1000:
    if num % 10 != 0:
        print(num - (num % 10))
else:
    print("非三位數整數")

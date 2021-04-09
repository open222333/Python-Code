n = int(input('請輸入一個值：'))
m = int(input('請輸入一個大於%d的值：' % n))
sum = 0
if n > m:
    print('數值輸入錯誤')
else:
    for i in range(n, m + 1):
        sum = sum + i

print('%d~%d總和為：%d' % (n, m, sum))

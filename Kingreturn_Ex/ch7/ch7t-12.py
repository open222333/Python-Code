lenth = 6
nntitle = '九九乘法表'
print(nntitle.center(lenth * 9, '-'))
formula = '%d*%d=%2d'
for i in range(1, 10):
    for j in range(1, 10):
        print(formula % (j, i, i * j), end=' ')
    print()

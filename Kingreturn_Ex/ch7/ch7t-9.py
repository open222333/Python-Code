# Euler's number
i = 100
euler_number = 1 # 歐拉數第一個 1
for x in range(1, i + 1):
    denominator = 1  # 分母
    for y in range(1, x + 1): # 計算階層
        denominator = denominator * y 
    euler_number += (1 / denominator)
    if x % 10 == 0:
        print('第%d次 值為%f' % (x, euler_number))

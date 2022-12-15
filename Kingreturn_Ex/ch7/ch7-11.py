# 擴充ch2_5.py 列出每年本金和變化
money = 50000
rate = 0.015
n = 5
for i in range(n):
    money *= (1 + rate)
    print('第%d本金和是：%d' % ((i + 1, int(money))))

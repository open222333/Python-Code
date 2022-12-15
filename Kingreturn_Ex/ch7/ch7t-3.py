# 擴充ch2_5.py 列出每年本金和變化
money = int(input('請輸入本金：'))
rate = float(input('請輸入年利率(％)：')) / 100
n = int(input('請輸入存款年數：'))
for i in range(n):
    money *= (1 + rate)
    print('第%d本金和是：%d' % ((i + 1, int(money))))

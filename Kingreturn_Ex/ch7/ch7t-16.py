# 最大公約數
x = int(input('輸入第一個數'))
y = int(input('輸入第二個數'))
# 紀錄因數
x_list = []
y_list = []
allin_list = []  # 紀錄共有的公因數
# 將兩個數的因數解析出來
for i in range(1, x):
    if x % i == 0:
        x_list.append(i)
for j in range(1, y):
    if y % j == 0:
        y_list.append(j)
# 找出最大公約數
for z in x_list:
    if z in y_list:
        allin_list.append(z)
print('最大公約數 ＝ ', max(allin_list))

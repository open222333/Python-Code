# 雞兔同籠
h = eval(input('請輸入頭的數量:'))
f = eval(input('請輸入腳的數量:'))
chicken = f / 2 - h
rabbit = 2 * h - f / 2
print('幾有{}隻, 兔有{}隻'.format(chicken, rabbit))

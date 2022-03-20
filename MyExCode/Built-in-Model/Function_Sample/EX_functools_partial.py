from functools import partial


'''
高階函數
https://www.runoob.com/w3cnote/python-partial.html'''


def mod(n, m):
    return n % m


mod_by_100 = partial(mod, 100)
print(mod(100, 7))
print(mod_by_100(7))

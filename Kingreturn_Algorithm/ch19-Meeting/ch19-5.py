# 遞迴式函數 歐幾里德演算法

def gcd(a, b):
    '''輾轉相除法求最大公約數'''
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def lcm(a,  b):
    '''最小公倍數'''
    return a * b // gcd(a, b)

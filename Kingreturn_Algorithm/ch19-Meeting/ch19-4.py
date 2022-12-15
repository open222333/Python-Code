# 輾轉相除法
def gcd(a, b):
    '''輾轉相除法求最大公約數'''
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

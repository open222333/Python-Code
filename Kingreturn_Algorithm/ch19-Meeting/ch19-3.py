# 歐幾里得演算法
def gcd(n1, n2):
    '''最大公約數'''
    g = 1  # 最初化最大公約數
    n = 2  # 從2開始檢測
    while n <= n1 and n <= n2:
        if n1 % n == 0 and n2 % n == 0:
            g = n  # 新最大公約數
        n += 1
    return g

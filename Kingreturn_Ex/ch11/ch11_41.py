# 專題 最大公約數 Greatest Common Divisor
def GCD(n1, n2):
    gcd = 1  # 最初化最大公約數
    n = 2  # 從2開始檢測
    while n <= n1 and n <= n2:
        if n1 % n == 0 and n2 % n == 0:
            gcd = n  # 新的最大公約數
        n += 1
    return gcd


n1, n2 = eval(input("請輸入2個整數值："))
print("最大公約數是：", GCD(n1, n2))

# 費波那契數列(Fibonacci)

def fibonacci(i):
    '''計算 費波那契數列(Fibonacci)'''
    if i == 0:  # 定義0
        return 0
    elif i == 1:  # 定義1
        return 1
    else:  # 執行遞迴計算
        return fibonacci(i - 1) + fibonacci(i - 2)


n = eval(input("請輸入 Fibonacci number:"))
for i in range(n + 1):
    print("n = {}, Fib({}) = {}".format(i, i, fibonacci(i)))

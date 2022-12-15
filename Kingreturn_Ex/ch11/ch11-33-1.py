# lambda函數 更加時機存在於一個函數內部
def func(b):
    return lambda x: 2 * x + b


linear = func(5)  # 5將傳給lambda的b
print(linear(10))  # 10 是lambda的x

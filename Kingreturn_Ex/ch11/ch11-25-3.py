# 函數可以當作參數傳遞給其他函數
def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def running(func, arg1, arg2):
    return func(arg1, arg2)


result1 = running(add, 5, 10)  # add函數當作參數
print(result1)
result2 = running(mul, 5, 10)  # mul函數當作參數
print(result2)

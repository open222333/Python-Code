# closure 另一個應用
def outer(a, b):
    '''a和b將是inner()的環境變數'''
    def inner(x):
        return a * x + b
    return inner


f1 = outer(1, 2)
f2 = outer(3, 4)
print(f1(1), f2(3))

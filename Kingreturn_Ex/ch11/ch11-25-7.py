# 閉包closure 記住函數以外所建立的環境變數值
def outer():
    b = 10  # inner所使用的變數值 與inner形成closure

    def inner(x):
        return 5 * x + b
    return inner


b = 2  # 作用在inner內的x
f = outer()
print(f(b))

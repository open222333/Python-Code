# 函數當參數與*args不定量的參數
def mysum(*args):
    return sum(args)


def run_with_multiple_args(func, *args):
    return func(*args)


print(run_with_multiple_args(mysum, 1, 2, 3, 4, 5))
print(run_with_multiple_args(mysum, 6, 7, 8, 9))

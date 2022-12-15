# 由函數呼叫了解語言的運作
def bye():
    print('下回見')


def system(name):
    print("%s 歡迎進入校友會系統" % name)


def welcome(name):
    print("%s 歡迎進入明志科技大學系統" % name)
    system(name)
    print("使用明志科技大學系統很棒")
    bye()


welcome("洪錦魁")

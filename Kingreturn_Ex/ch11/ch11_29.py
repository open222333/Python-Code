# 區域變數無法在其他函數引用
def defmsg():
    msg = 'pringmsg variable'

def printmsg():
    # print(msg) # 列印defmsg()函數定義的區域函數
    pass

printmsg()
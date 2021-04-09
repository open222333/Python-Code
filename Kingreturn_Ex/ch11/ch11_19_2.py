# 觀察傳遞一般變數與串列變數到函數的區別
def mydata(n):
    print("函  數 id(n) = :", id(n), '\t', n)
    n[0] = 5  # 更改了串列內容
    print("函  數 id(n) = :", id(n), "\t", n)


x = [1, 2]
print("主程式 id(x) = :", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = :", id(x), "\t", x)

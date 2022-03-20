# 函數可以是資料結構的成員
def total(data):
    return sum(data)


x = (1, 5, 10)
# 內建函數會出現<build-in ...> 非內建函數則列出記憶體位址
myList = [min, max, sum, total]
for f in myList:
    print(f)

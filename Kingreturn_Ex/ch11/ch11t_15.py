# 使用匿名函數重新設計 filter(func,iterable) 篩選物件
mylist = [5, 10, 15, 20, 25, 30]
oddlist = list(filter(lambda x: (x % 2 == 0), mylist))

# 輸出偶數串列
print("偶數串列：", oddlist)

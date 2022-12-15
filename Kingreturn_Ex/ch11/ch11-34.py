# 匿名函數使用與filter() 使用傳統定義方式將串列元素內容是奇數的元素篩選出來
def oddfn(x):
    return x if (x % 2 == 1) else None


mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)  # 傳回filter object

# 輸出奇數串列
print("奇數串列:", [item for item in filter_object])

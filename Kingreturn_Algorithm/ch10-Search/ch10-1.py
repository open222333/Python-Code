# 順序搜尋法(Sequentail Search)

def sequentail_search(nLst, key):
    for i in range(len(nLst)):
        if nLst[i] == key:
            return i
    return -1


data = [6, 1, 5, 7, 3, 9, 4, 2, 8]
key = eval(input("請輸入搜尋值："))
index = sequentail_search(data, key)
if index != -1:
    print("在%d索引位置找到了工找了%d次" % (index, (index + 1)))
else:
    print("查無此搜尋號碼")

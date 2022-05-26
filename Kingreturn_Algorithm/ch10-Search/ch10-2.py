# 二分搜尋法(Binary Search)

def binary_search(nLst: list, key):
    nLst.sort()
    print('列印搜尋串列：', nLst)
    low = 0  # 串列最小索引
    high = len(nLst) - 1  # 串列最大索引
    middle = int((high + low) / 2)  # 中間索引
    times = 0  # 搜尋次數
    while True:
        times += 1
        if key == nLst[middle]:  # 找到了
            return middle, times
        elif key > nLst[middle]:
            low = middle + 1  # 下一次往右搜尋
        else:
            high = middle - 1  # 下一次往左搜尋
        middle = int((high + low) / 2)  # 更新中間索引
        if low > high:  # 所有元素比較結束
            return -1, times


data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
key = eval(input('請輸入要搜尋的值：'))
index, times = binary_search(data, key)
if index != -1:
    print("在%d索引位置找到了共找了%d次" % (index, times))
else:
    print("查無此搜尋號碼")

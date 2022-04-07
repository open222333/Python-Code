# 選擇排序法(Selection Sort)
'''將最小值與最小索引值對調'''


def selection_sort(nLst):
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index] > nLst[j]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更動
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
        print("第 %d 次 迴圈排序" % (i + 1), nLst)
    return nLst


data = [6, 1, 5, 7, 3]
print("原始串列：", data)
print("排序結果：", selection_sort(data))

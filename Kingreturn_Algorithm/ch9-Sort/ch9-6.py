# 為含字串的串列執行選擇性排序

def selection_sort(nLst):
    '''選擇排序法'''
    for i in range(len(nLst) - 1):
        index = i
        for j in range(i + 1, len(nLst)):
            if nLst[index] > nLst[j]:
                index = j
        if i == index:
            pass
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]
        print("第 %d 次 迴圈排序" % (i + 1), nLst)
    return nLst


cars = ['nonda', 'bmw', 'toyota', 'ford']
print("目前串列內容 = ", cars)
print("使用selection_sort()由小排到大")
selection_sort(cars)
print("排序串列結果 = ", cars)

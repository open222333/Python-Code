# 快速排序(Quick Sort)

def quick_sort(nLst):
    '''快速排序(Quick Sort)

    1. 挑出基準(pivot)
    2. 排序 比基準小排左邊 比基準大排右邊
    3. 遞迴式針對兩辮子序列做相同程序
    '''
    import random

    if len(nLst) <= 1:
        return nLst

    left = []  # 左邊串列
    right = []  # 右邊串列
    piv = []  # 基準串列
    pivot = random.choice(nLst)  # 隨機設定基準
    for val in nLst:  # 分類
        if val == pivot:
            piv.append(val)  # 加入基準串列
        elif val < pivot:  # 如果小於基準
            left.append(val)  # 加入左邊串列
        else:
            right.append(val)  # 加入右邊串列
    return quick_sort(left) + piv + quick_sort(right)


data = [6, 1, 5, 7, 3, 9, 4, 2, 8]
print("原始串列:", data)
print("排列結果:", quick_sort(data))

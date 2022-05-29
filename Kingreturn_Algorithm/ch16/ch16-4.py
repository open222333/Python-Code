# 動態規劃演算法


def knapsack(W, wt, val):
    '''動態規劃演算法'''
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格
    for r in range(n + 1):  # 填入表格column
        for c in range(W + 1):  # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r - 1] <= c:
                table[r][c] = max(val[r - 1] + table[r - 1][c - wt[r - 1]], table[r - 1][c])
            else:
                table[r][c] = table[r - 1][c]
    return table[n][W]


value = [7, 6, 9, 9, 8]  # 旅遊點評分數
weight = [1, 1, 2, 4, 1]  # 單向景點所需天數
travel_weight = 4  # 總旅遊天數
print('旅遊點評總分:', knapsack(travel_weight, weight, value))

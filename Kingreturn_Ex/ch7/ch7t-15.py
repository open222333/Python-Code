# while迴圈條件運算式 與 可迭代物件
buyers = [['James', 1030], ['Curry', 893], ['Durant', 2050],
          ['Jordan', 990], ['David', 2110], ['Kevin', 15000],
          ['Mary', 10050], ['Tom', 8800]]  # 建立買家購買紀錄
goldbuyers = []  # Gold買家串列
vipbuyers = []  # VIP買家串列
infinitebuyers = []  # 10000以上歸類的買家串列
while buyers:  # 執行買家分類迴圈分類完成迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 10000:  # 用10000元執行買家分類條件
        infinitebuyers.append(index_buyer)
    elif index_buyer[1] >= 1000:  # 用1000元執行買家分類條件
        vipbuyers.append(index_buyer)
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("INFINTE買家資料", infinitebuyers)
print("VIP買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)

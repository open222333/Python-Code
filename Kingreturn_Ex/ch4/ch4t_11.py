# 重新設計ch3_26.py 輸入座標計算2點距離
x1, y1 = eval(input("輸入第一個座標，使用逗號分開："))
x2, y2 = eval(input("輸入第二個座標，使用逗號分開："))
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(distance)

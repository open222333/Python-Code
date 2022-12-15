# 輸入三點座標 計算三角形面積
x1, y1 = eval(input("第一點座標："))
x2, y2 = eval(input("第二點座標："))
x3, y3 = eval(input("第三點座標："))
dist1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
dist2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
dist3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
p = (dist1 + dist2 + dist3) / 2
area = (p * (p - dist1) * (p - dist2) * (p - dist3)) ** 0.5
print("三角形面積為：", area)

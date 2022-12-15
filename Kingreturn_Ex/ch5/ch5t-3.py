# 輸入一個座標 判斷是否在圓內
x, y = eval(input("請輸入座標："))
distance = (x ** 2 + y ** 2) ** 0.5  # 輸入座標與圓中心的距離
r = 20  # 圓半徑
if distance < r:
    print("輸入的座標在圓內")
else:
    print("輸入的座標不在圓內")

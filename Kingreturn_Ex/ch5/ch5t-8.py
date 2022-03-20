# 輸入三個邊長 判斷是否為三角形 是則輸出周長 否則輸出無法形成三角形
dist1, dist2, dist3 = eval(input("請輸入三個邊長："))
if dist1 + dist2 <= dist3 or dist1 + dist3 <= dist2 or dist2 + dist3 < dist1:
    print("無法形成三角形")
else:
    print("周長：", dist1 + dist2 + dist3)

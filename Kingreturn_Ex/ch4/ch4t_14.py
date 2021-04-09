import math

r = 6371  # 地球半徑
x1, y1 = eval(input("第一個地點經緯度："))
x2, y2 = eval(input("第二個地點經緯度："))
d = 6371 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                              math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                              math.cos(math.radians(y1 - y2)))
print("distance = ", d)
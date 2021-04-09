import math

r = 6371  # 地球半徑
x1, y1 = 22.2838, 114.1731
x2, y2 = 25.0452, 121.5168
d = 6371 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                              math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                              math.cos(math.radians(y1 - y2)))
print("distance = ", d)

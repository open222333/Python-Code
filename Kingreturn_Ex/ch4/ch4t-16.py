import math

r = 6371  # 地球半徑
x1, y1 = 39.9196, 116.3669
x2, y2 = 48.8595, 2.3369
d = 6371 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                     math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                     math.cos(math.radians(y1 - y2)))
print("distance = ", d)

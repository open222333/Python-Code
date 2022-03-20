# 重新設計ch3_26.py
def pointto00(x, y):
    dist = (x ** 2 + y ** 2) ** 0.5
    return dist


x1, y1 = 1, 8
x2, y2 = 3, 10
print(pointto00(x1, y1), pointto00(x2, y2))

# 輸入正五角形的邊長 會計算正五角形的面積
import math

s = eval((input("請輸入正五角型的邊長：")))
area = (5 * s ** 2) / (4 * math.tan(math.pi / 5))
print("area = ", area)

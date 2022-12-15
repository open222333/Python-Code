# 輸入正n邊形的邊長 輸出面積
import math

s = eval(input("請輸入邊長："))
n = eval(input("正多邊形邊數："))
area = (n * (s ** 2)) / (4 * math.tan(math.pi / n))
print(area)
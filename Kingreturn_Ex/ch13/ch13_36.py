# 利用參數是int的特性建立計數器
from collections import defaultdict

fruits = defaultdict(int)
for fruit in ["apple", "orange", "apple"]:
    fruits[fruit] += 1

for fruit, count in fruits.items():
    print(fruit, count)

# choice() 從串列中隨機傳回一個元素
import random  # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
while True:
    fruit = random.choice(fruits)
    print(fruit)
    fruits.remove(fruit)
    if len(fruits) == 0:
        break

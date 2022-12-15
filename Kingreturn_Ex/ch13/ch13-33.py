# collections模組 defaultdict() 建立新字典並設定預設值
from collections import defaultdict

fruits = defaultdict(int)
fruits['apple'] = 20
fruits["orange"]  # 使用int預設的0
print(fruits["apple"])
print(fruits["orange"])
print(fruits)

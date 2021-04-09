# 使用lambda重新設計
from collections import defaultdict

fruits = defaultdict(lambda: 10)
fruits['apple'] = 20
fruits['orange']  # 使用lambda設定的10
print(fruits['apple'])
print(fruits['orange'])
print(fruits)

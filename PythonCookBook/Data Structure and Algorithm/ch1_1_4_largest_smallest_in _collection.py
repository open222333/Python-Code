'''
1.4 找出最大或最小的Ｎ個項目
問題：
找出一個群集(collection)中最大或最小的Ｎ個項目做成一個串列(list)
解法：
heapq模組 nlargest() nsmallest()
討論：
heapq運作方式：先將資料轉為一個串列，項目以堆積(heap)的形式安置的。
'''
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
heap = list(nums)
heapq.heapify(heap)
print(heapq.heappop())  # 取出第一個項目

portfollo = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfollo, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfollo, key=lambda s: s['price'])

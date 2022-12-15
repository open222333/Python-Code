'''堆積的元素是元組'''
import heapq

h = []
heapq.heappush(h, (100, "牛肉麵"))
heapq.heappush(h, (60, "陽春麵"))
heapq.heappush(h, (80, "肉絲麵"))
heapq.heappush(h, (90, "大滷麵"))
heapq.heappush(h, (70, "家常麵"))
print(h)
print(heapq.heappop(h))

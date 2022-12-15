'''從堆積取出和刪除元素heappop()'''
import heapq


h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("取出前 h = ", h)
val = heapq.heappop(h)
print("取出元素 = ", val)
print("取出後 h = ", h)

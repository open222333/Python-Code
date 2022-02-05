'''堆入和取出heappushpop()'''
import heapq
h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("堆入和取出前 h = ", h)
val = heapq.heappushpop(h, 11)
print("取出元素 = ", val)
print("堆入和取出後 h = ", h)

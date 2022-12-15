# 取出堆積的最小值和插入新元素
import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("執行前 h = ", h)
x = heapq.heapreplace(h, 7)
print("取出值 = ", x)
print("執行後 h = ", h)

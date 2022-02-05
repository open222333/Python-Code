# nlargest() nsmallest() 傳回最大值和最小值的應用
import heapq

h = [10, 21, 5, 9, 13, 28, 3]
print("最大3個:", heapq.nlargest(3, h))
print("最小3個:", heapq.nsmallest(3, h))
print("原先資料集:", h)

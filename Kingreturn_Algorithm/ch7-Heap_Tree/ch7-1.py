'''建立二元堆積樹'''
import heapq


h = [10, 21, 5, 9, 13, 28, 3]
print("執行前 h = ", h)
heapq.heapify(h)
print("執行後 h = ", h)

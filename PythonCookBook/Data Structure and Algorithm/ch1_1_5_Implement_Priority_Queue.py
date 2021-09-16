import heapq
'''
1.5 實作一個優先序佇列
問題：
實作一個佇列(queue)，依據給定的優先序(priority)排序項目，每次取出(pop)都回傳最高優先序的項目
解法：
用heapq模組實作簡單的優先序佇列
討論：
heapq.heappush() 插入項目
heapq.heappop() 回傳那個最小的項目
佇列由(-priority, index, item)這種形式的元組(tuples)，取負的priority使項目從最高優先序排到最低優先序
Item實體(instances)是無法比較。
(priority, item)元組，可比較，若有相同優先序就會無法比較。
(priority, index, item)可以比較且因元組不會有相同的index，不會有無法比較的問題。
'''


class ProiorityQueue:
    '''用heapq模組實作簡單的優先序佇列'''

    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 使用ProiorityQueue
class Item:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return 'Item({!r})'.format(self.name)


q = ProiorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# Item實體無法比較
a = Item('foo')
b = Item('bar')
# print(a < b) # 出現錯誤

# (priority, item)元組，可比較，若有相同優先序就會無法比較。
a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)
c = (1, Item('grok'))
# 若有相同優先序就會無法比較。
# print(a < c) # 出現錯誤

# (priority, index, item)可以比較且因元組不會有相同的index，不會有無法比較的問題。
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
print(a < c)

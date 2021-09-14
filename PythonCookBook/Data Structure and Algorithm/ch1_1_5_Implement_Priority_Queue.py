import heapq


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

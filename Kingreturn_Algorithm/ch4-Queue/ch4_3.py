# 跟佇列有關的Python模組
from queue import Queue


q = Queue()
for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())

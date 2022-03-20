# 使用串列模擬佇列的操作
# 擴充ch4_1.py 讀取4次佇列
class Queue():
    '''Queue 佇列'''

    def __init__(self) -> None:
        self.queue = []  # 使用串列模擬

    def enqueue(self, data):
        '''讀取佇列'''
        self.queue.insert(0, data)

    def dequeue(self):
        '''讀取佇列'''
        if len(self.queue):
            return self.queue.pop()
        return "佇列是空的"


q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print("讀取佇列：", q.dequeue())
print("讀取佇列：", q.dequeue())
print("讀取佇列：", q.dequeue())
print("讀取佇列：", q.dequeue())

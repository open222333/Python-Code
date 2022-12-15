# 使用串列模擬佇列的操作
class Queue():
    '''Queue佇列'''

    def __init__(self) -> None:
        self.queue = []  # 使用串列模擬

    def enqueue(self, data):
        '''data 插入佇列'''
        self.queue.insert(0, data)

    def size(self):
        '''回傳佇列長度'''
        return len(self.queue)


q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print('佇列長度是：', q.size())

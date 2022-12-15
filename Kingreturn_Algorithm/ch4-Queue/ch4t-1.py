class Queue():
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
        print(f"成功插入 {data} 至佇列")

    def get_size(self):
        return f'佇列的長度是： {len(self.queue)}'


q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print(q.get_size())

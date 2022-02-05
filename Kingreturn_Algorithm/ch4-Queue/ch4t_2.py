from queue import Queue

items = ['漢堡', '薯條', '可樂']
q = Queue()

for item in items:
    q.put(item)
    print(f'成功插入 {item} 至佇列')

print('佇列輸出')
while not q.empty():
    print(q.get())

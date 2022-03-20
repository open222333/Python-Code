# 自行建立Stack類別執行相關操作
# 設計get() 傳回堆疊頂端值不刪除
class Stack():
    def __init__(self) -> None:
        self.my_stack = []

    def my_push(self, data):
        self.my_stack.append(data)

    def my_pop(self):
        return self.my_stack.pop()

    def size(self):
        return len(self.my_stack)

    def isEmpty(self):
        return self.my_stack == []

    def get(self):
        print(f'堆疊取出 {self.my_stack[self.size() - 1]} 水果，同時不刪除')


stack = Stack()
fruits = ['Grape', 'Mango', 'Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print("將 %s 水果堆入堆疊" % fruit)

print("堆疊有 %d 種水果" % stack.size())
for i in range(0, 3):
    stack.get()
while not stack.isEmpty():
    print(stack.my_pop())

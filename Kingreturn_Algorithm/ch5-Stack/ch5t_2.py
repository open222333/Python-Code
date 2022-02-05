# 自行建立Stack類別執行相關操作
# 新增cls() 刪除所有堆疊資料
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

    def cls(self):
        self.my_stack = []


stack = Stack()
fruits = ['Grape', 'Mango', 'Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print("將 %s 水果堆入堆疊" % fruit)

print("堆疊有 %d 種水果" % stack.size())
stack.cls()
while not stack.isEmpty():
    print(stack.my_pop())

print('程式結束')

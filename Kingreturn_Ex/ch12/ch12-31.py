# __iter__() Fib序列數
class Fib():
    def __init__(self, max):
        self.max = max

    def __iter__(self):  # 將類別定義為一個迭代物件
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration  # 達到結束條件 終止繼續
        self.a, self.b = self.b, self.a + self.b
        return fib


for i in Fib(100):
    print(i)

class Test():
    '''
    __call__ 使 class 可以像函式一樣被呼叫使用
    self()呼叫 Test
    '''

    def __init__(self) -> None:
        self.num = None

    def __call__(self):
        print(f'{self.num}')
        pass

    def done(self):
        self()


t = Test()
t.num = 1
print(t.num)
t.done()

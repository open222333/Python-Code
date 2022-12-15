# 方法與屬性的類型
# 類別方法 參數習慣使用cls
class Counter():
    counter = 0  # 類別屬性,可由類別本身調用

    def __init__(self):
        Counter.counter += 1  # 更新指標

    @classmethod
    def show_counter(cls):  # 類別方法,可由類別本身調用
        print("class method")
        print("counter = ", cls.counter)  # 也可使用Counter.counter調用
        print("counter = ", Counter.counter)

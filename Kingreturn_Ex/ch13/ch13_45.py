# chain() 將參數的元素內容一一迭代出來
import itertools
for i in itertools.chain([1, 2, 3], ('a', 'd')):
    print(i)

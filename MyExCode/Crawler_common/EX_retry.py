from retry import retry
import random

# retry套件範例 有異常就重試

@retry(delay=1)
def test():
    print(random.randint(0, 10) / random.randint(0, 10))

# print(not bool(0))

n = 100
while True:
    if n == 0:
        break
    print(n)
    test()

    n -= 1

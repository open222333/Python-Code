# 設計自己的range()
def myRange(start=0, stop=100, step=1):
    n = start
    while n < stop:
        yield n
        n += step


print(type(myRange))
for x in myRange(0, 5):
    print(x)

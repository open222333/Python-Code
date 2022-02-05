from array import *

x = array('i', [5, 15, 25, 35, 45])
n = x.pop()
print('刪除', n)
for data in x:
    print(data)

n = x.pop(2)
print('刪除', n)
for data in x:
    print(data)

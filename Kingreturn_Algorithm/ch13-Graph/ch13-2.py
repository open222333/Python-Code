# 使用collections模組 deque() 資料結構中的雙頭序列
# append(x):從右邊加入元素x
# appendleft(x):從左邊加入元素x
# pop():移除右邊的元素並回傳
# popleft():移除左邊的元素並回傳
# clear():清空所有元素

from collections import deque

graph = {}
graph['Tom'] = ['Ivan', 'Ira', 'Kevin']
people = deque()
people += graph['Tom']
print('列出people資料類型:', type(people))
print('列出搜尋名單:', people)
for name in range(len(people)):
    print(people.pop())

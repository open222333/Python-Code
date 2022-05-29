# 使用collections模組 deque() 資料結構中的雙頭序列
# append(x):從右邊加入元素x
# appendleft(x):從左邊加入元素x
# pop():移除右邊的元素並回傳
# popleft():移除左邊的元素並回傳
# clear():清空所有元素

from collections import deque

people = deque()
people.append('Ivan')
people.append('Ira')
print('列出名單:', people)
people.appendleft('Unistar')
print('列出名單:', people)
people.appendleft('Ice Rain')
print('列出名單:', people)
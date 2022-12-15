# 廣度優先搜尋演算法(Breadth First Search - BFS)
# 使用collections模組 deque() 資料結構中的雙頭序列
# append(x):從右邊加入元素x
# appendleft(x):從左邊加入元素x
# pop():移除右邊的元素並回傳
# popleft():移除左邊的元素並回傳
# clear():清空所有元素

from collections import deque


def banana_dealer(name):
    '''回應是否賣香蕉的經銷商'''
    if name == 'Banana':
        return True


def search(name):
    '''搜尋賣香蕉的朋友'''
    global not_dealer  # 儲存已搜尋的名單
    dealer = deque()
    dealer += graph[name]  # 搜尋串列先儲存Tom的朋友
    while dealer:
        person = dealer.popleft()
        if banana_dealer(person):
            print(person + '是香蕉經銷商')
            return True
        else:
            not_dealer.append(person)  # 將搜尋過的人儲存至串列d
            dealer += graph[person]  # 將不是經銷商的朋友加入搜尋串列
    print('沒有找到經銷商')
    return False


not_dealer = []
graph = {}
graph['Tom'] = ['Ivan', 'Ira', 'Kevin']
graph['Ivan'] = ['Peter']
graph['Ira'] = ['Banana']
graph['Kevin'] = ['Mary']
graph['Peter'] = []
graph['Banana'] = []
graph['Mary'] = []

search('Tom')
print('列出已搜尋名單:', not_dealer)

# 廣度優先搜尋演算法(Breadth First Search - BFS)
# 有缺陷的
# 單向佇列


def bfs(graph, start):
    '''廣度優先搜尋演算法(Breadth First Search - BFS)'''
    visited = []  # 拜訪過的頂點
    queue = [start]  # 模擬佇列
    while queue:
        node = queue.pop(0)  # 取索引0的值
        visited.append(node)  # 加入已拜訪行列
        neighbors = graph[node]  # 取得已拜訪節點的相鄰節點
        for n in neighbors:  # 將相鄰節點放入佇列
            queue.append(n)
    return visited


not_dealer = []
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'J'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
}

print(bfs(graph, 'A'))

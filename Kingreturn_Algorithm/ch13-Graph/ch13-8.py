# 使用廣度優先搜尋法走迷宮

def is_exit(node):
    '''是否為迷宮出口'''
    if node == 'K':
        return True


def bfs(graph, start):
    '''廣度優先搜尋法'''
    global visited  # 拜訪過的頂點
    queue = [start]  # 模擬佇列
    while queue:
        node = queue.pop(0)  # 取索引0的值
        if is_exit(node):
            print(node + '是迷宮出口')
            visited.append(node)  # 將出口加入已拜訪
            return visited  # bfs()結束
        if node not in visited:
            visited.append(node)  # 加入已拜訪行列
            neighbors = graph[node]  # 取得已拜訪節點的相鄰節點
            for n in neighbors:  # 將相鄰節點加入佇列
                queue.append(n)
    return visited


graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'E'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['G'],
    'G': ['F', 'H', 'J'],
    'H': ['E', 'G', 'I'],
    'I': ['H', 'K'],
    'J': ['G'],
    'K': ['I']
}
visited = []
print(bfs(graph, 'A'))

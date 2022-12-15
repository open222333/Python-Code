# 深度優先搜尋演算法
def dfs(graph, start, goal):
    '''深度優先搜尋法'''
    path = []  # 拜訪過的節點
    stack = [start]  # 模擬堆疊
    while stack:
        node = stack.pop()  # pop堆疊
        path.append(node)  # 加入已拜訪的行列
        if node == goal:  # 如果找到了
            print('找到了')
            return path
        for n in graph[node]:
            stack.append(n)
    return '找不到'


graph = {
    'A': ['D', 'C', 'B'],
    'B': ['E'],
    'C': ['F'],
    'D': ['H', 'G'],
    'E': [],
    'F': ['J', 'I'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}
print(dfs(graph, 'A', 'G'))

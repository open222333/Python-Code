# 使用遞迴遍歷無方向節點

def dfs(graph, node, path=[]):
    '''深度優先搜尋法'''
    path += [node]  # 路徑
    for n in graph[node]:  # 將相鄰節點放入佇列
        if n not in path:
            path = dfs(graph, n, path)
    return path


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'H', 'G'],
    'E': ['B'],
    'F': ['C', 'J', 'I'],
    'G': ['D'],
    'H': ['D'],
    'I': ['F'],
    'J': ['F']
}
print(dfs(graph, 'A'))

'''
> ## 深度優先搜尋(Depth First Search - DFS)
> 
> 說明：這個演算法會儘可能深的搜尋樹的分支
> 
> 檔案：EX_DepthFirstSearch.py

https://github.com/25349023/Blogger/blob/master/DFS/dfs1.py
'''


class Node():
    def __init__(self, s) -> None:
        self.data = s
        self.next = [None, None, None]
        pass


def build_tree():
    # 建立範例 樹
    root = Node('red-1')
    root.next[0] = Node('orange-2')
    root.next[1] = Node('lime-3')
    root.next[2] = Node('green-4')
    root.next[0].next[0] = Node('yellow-5')
    root.next[2].next[0] = Node('blue-6')
    root.next[2].next[1] = Node('violet-7')
    return root


def depthFirstSearch(start: Node):
    if start is None:
        return
    print(start.data, 'visited')
    for i in range(3):
        depthFirstSearch(start.next[i])


tree = build_tree()
depthFirstSearch(tree)

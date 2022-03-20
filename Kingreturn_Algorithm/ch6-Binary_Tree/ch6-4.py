'''遍歷二元樹使用中序(inorder)列印
LDR: 遍例左子樹(Left)、根節點(Root)、遍例右子樹(Right)'''


class Node():
    '''建立二元樹節點'''

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:  # 若根節點存在
            if data < self.data:  # 插入值小於目前節點
                if self.left:
                    self.left.insert(data)  # 遞迴呼叫下一層
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:  # 若根節點不存在
            self.data = data

    def inorder(self):
        '''中序列印'''
        if self.left:  # 如果左子節點存在
            self.left.inorder()  # 遞迴呼叫下一層
        print(self.data)  # 列印
        if self.right:  # 如果右子節點存在
            self.right.inorder()  # 遞迴呼叫下一層


tree = Node()  # 建立二元樹物件
datas = [10, 21, 5, 9, 13, 28]  # 建立二元樹數據
for d in datas:
    tree.insert(d)  # 分別插入數據
tree.inorder()  # 中序列印

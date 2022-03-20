'''遍例二元樹使用前序
DLR: 根節點(Root)、遍例左子樹(Left)、遍例右子樹(Right)'''


class Node():
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
                    self.left = Node(data)  # 建立新節點存放新資料
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def preorder(self):
        '''前序列印'''
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


tree = Node()
datas = [10, 21, 5, 9, 13, 28]  # 建立二元樹數據
for d in datas:
    tree.insert(d)
tree.preorder()

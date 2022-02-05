'''遍例二元樹使用前序
LRD: 遍例左子樹(Left)、遍例右子樹(Right)、根節點(Root)'''


class Node():

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def postorder(self):
        '''後序列印'''
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)


tree = Node()
datas = [10, 21, 5, 9, 13, 28]  # 建立二元樹數據
for d in datas:
    tree.insert(d)
tree.postorder()

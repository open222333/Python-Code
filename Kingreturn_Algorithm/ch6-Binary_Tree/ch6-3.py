'''鏈結串列方式建立二元樹的根節點'''


class Node():

    def __init__(self, data) -> None:
        '''建立二元樹的節點'''
        self.data = data
        self.left = None
        self.right = None

    def print_root(self):
        print(self.data)

    def insert(self, data):
        '''使用鏈結串列建立二元樹'''
        if self.data:  # 如果根節點存在
            if data < self.data:  # 插入值小於目前節點值
                if self.left:
                    self.left.insert(data)  # 遞迴呼叫往下一層
                else:
                    self.left = Node(data)  # 建立新節點存放資料
            else:  # 插入值大於目前節點值
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:  # 如果根節點不存在
            self.data = data  # 建立根節點


root = Node(20)
root.print_root()

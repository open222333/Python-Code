'''二元樹的搜尋'''


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

    def search(self, val):
        '''搜尋特定值'''
        if val < self.data:  # 如果搜尋值小於目前節點值
            if not self.left:
                return str(val) + "不存在"
            return self.left.search(val)
        elif val > self.data:
            if not self.right:
                return str(val) + "不存在"
            return self.right.search(val)
        else:
            return str(val) + "找到了"


tree = Node()
datas = [10, 21, 5, 9, 13, 28]  # 建立二元樹數據
for d in datas:
    tree.insert(d)

n = eval(input("請輸入欲搜尋的資料:"))
print(tree.search(n))

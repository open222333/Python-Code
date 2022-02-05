# 建立循環鏈結串列
class Node():
    '''節點'''

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標


n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
n1.next = n2
n2.next = n3
n3.next = n1
ptr = n1  # 建立指標節點
counter = 1
while counter <= 6:  # 列印6次
    print(ptr.data)  # 列印節點
    ptr = ptr.next  # 移動指標到下一個節點
    counter += 1

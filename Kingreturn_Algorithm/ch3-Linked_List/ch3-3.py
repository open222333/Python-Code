# 在第一個節點前插入一個新的節點
class Node():
    '''節點'''

    def __init__(self, data=None) -> None:
        self.data = data  # 資料
        self.next = None  # 指標


class Linked_list():
    '''鏈結串列'''

    def __init__(self) -> None:
        self.head = None  # 鏈結串列第1個節點

    def print_list(self):
        '''列印鏈結串列'''
        ptr = self.head  # 指標指向鏈結串列第1個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def begining(self, newdata):
        '''在第1個節點前插入新節點'''
        new_node = Node(newdata)  # 建立新節點
        new_node.next = self.head  # 新節點指標指向舊的第1個節點
        self.head = new_node


link = Linked_list()
link.head = Node(5)
n2 = Node(15)  # 節點2
n3 = Node(25)  # 節點3
link.head.next = n2  # 節點1 指向 節點2
n2.next = n3  # 節點2 指向 節點3
link.print_list()  # 列印鏈結串列 link
print("新的鏈結串列")
link.begining(100)  # 在第1個節點前插入新的節點
link.print_list()  # 列印新的鏈結串列 link

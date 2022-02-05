# 在鏈結串列中間插入新的節點
class Node():
    '''節點'''

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標


class Linked_list():
    '''鏈結串列'''

    def __init__(self):
        self.head = None  # 鏈結串列的第1個節點

    def print_list(self):
        '''列印鏈結串列'''
        ptr = self.head  # 指標指向鏈結串列的第1個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def between(self, pre_node, newdata):
        '''在串列兩個節點間插入新節點'''
        if pre_node == None:
            print("缺插入節點的前一個節點")
            return
        # 建立和插入新節點
        new_node = Node(newdata)  # 建立新節點
        new_node.next = pre_node.next  # 新建節點指向前一個節點的下一個節點
        pre_node.next = new_node  # 前一節點指向新建節點


link = Linked_list()
link.head = Node(5)
n2 = Node(15)  # 節點2
n3 = Node(25)  # 節點3
link.head.next = n2  # 節點1指向節點2
n2.next = n3  # 節點2指向節點3
link.print_list()  # 列印鏈結串列link
print("新的鏈結串列")
link.between(n2, 100)  # 在串列n2插入新的節點
link.print_list()  # 列印新的鏈結串列Link

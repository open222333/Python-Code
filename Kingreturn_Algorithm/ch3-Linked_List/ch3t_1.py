# 建立鏈結串列與遍歷此鏈結串列
class Node():
    '''節點'''

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標


class Linked_list():
    '''鏈結串列'''

    def __init__(self):
        self.head = None  # 鏈結串列的第一個節點

    def print_list(self):
        '''列印鏈結串列'''
        ptr = self.head  # 指標指向鏈結串列第一個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def length(self):
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count


link = Linked_list()
link.head = Node(5)  # 節點1
n2 = Node(15)  # 節點2
n3 = Node(25)  # 節點3
link.head.next = n2  # 節點1指向節點2
n2.next = n3
link.print_list()  # 列印鏈結串列 link
print("鏈結串列長度是：", link.length())

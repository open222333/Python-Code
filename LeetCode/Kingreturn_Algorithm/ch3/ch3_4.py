# 在鏈結串列末端加入一個新的節點
class Node():
    '''節點'''

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標


class Linled_list():
    '''鏈結串列'''

    def __init__(self):
        self.head = None  # 鏈結串列的第1個節點

    def print_list(self):
        '''列印鏈結串列'''
        ptr = self.head  # 指標指向鏈結第1個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def ending(self, newdata):
        '''在串列末端插入新節點'''
        new_node = Node(newdata)  # 建立新節點
        if self.head == None:  # 如果是True，表示鏈結串列是空的
            self.head = new_node  # 所以head就可以直接指向此新節點
            return
        last_ptr = self.head  # 設定最後指標是鏈結串列頭部
        while last_ptr.next:  # 移動指標直到最後
            last_ptr = last_ptr.next
        last_ptr.next = new_node  # 將最後一個節點的指標指向新節點


link = Linled_list()
link.head = Node(5)
n2 = Node(15)  # 節點2
n3 = Node(25)  # 節點3
link.head.next = n2  # 節點1指向節點2
n2.next = n3  # 節點2指向節點3
link.print_list()  # 列印鏈結串列link
print("新的鏈結串列")
link.ending(100)  # 在串列末端插入新的節點
link.print_list()  # 列印新的鏈結串列Link

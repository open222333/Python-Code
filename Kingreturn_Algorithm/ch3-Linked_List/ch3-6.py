# 在鏈結串列中移除指定內容的節點
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
        ptr = self.head  # 指標指向鏈結串列的第1個節點
        while ptr:
            print(ptr.data)  # 列印資料
            ptr = ptr.next  # 移動指標到下一個節點

    def ending(self, newdata):
        '''在串列末端插入新節點'''
        new_node = Node(newdata)  # 建立新節點
        while self.head == None:  # 如果是True, 表示鏈結串列是空的
            self.head = new_node
            return
        last_ptr = self.head  # 設定最後指標是鏈結串列頭部
        while last_ptr.next:  # 移動指標直到最後
            last_ptr = last_ptr.next
        last_ptr.next = new_node

    def rm_node(self, rmkey):
        '''刪除值是rmkey的節點'''
        ptr = self.head  # 暫時指標
        if ptr:
            if ptr.data == rmkey:
                self.head = ptr.next  # 將第一個指標指向下一個節點
                return
        while ptr:
            if ptr.data == rmkey:
                break

            prev = ptr  # 設定前一節點指標
            ptr = ptr.next  # 移動指標
        if ptr == None:  # 如果ptr已經是末端
            return  # 找不到所以返回
        prev.next = ptr.next  # 找到了所以將前一個節點指向下一個節點


link = Linked_list()
link.ending(5)
link.ending(15)
link.ending(25)
link.print_list()
print("新的鏈結串列")
link.rm_node(15)
link.print_list()

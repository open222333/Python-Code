class Node():

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None  # 下一個
        self.previous = None  # 上一個


class Linked_list():
    '''雙向鏈結'''

    def __init__(self) -> None:
        self.head = None  # 頭
        self.tail = None  # 尾

    def add_node(self, new_node):
        if isinstance(new_node, Node):
            if self.head == None:
                self.head = new_node
                new_node.previous = None
                new_node.next = None
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
        return

    def print_list_from_head(self):
        '''從頭部列印'''
        ptr = self.head
        print('從頭部列印雙向鏈結串列')
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def print_list_from_tail(self):
        '''從尾部列印'''
        ptr = self.tail
        print('從尾部列印雙向鏈結串列')
        while ptr:
            print(ptr.data)
            ptr = ptr.previous


link = Linked_list()
link.add_node(Node('Sun'))
link.add_node(Node('Mon'))
link.add_node(Node('Tue'))
link.add_node(Node('Web'))
link.add_node(Node('Thu'))
link.add_node(Node('Fri'))
link.add_node(Node('Sat'))
link.print_list_from_head()
link.print_list_from_tail()

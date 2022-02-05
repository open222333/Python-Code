class Node():
    '''節點'''

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 向前指標
        self.previous = None  # 向後指標


class Double_linked_list():
    '''鏈結串列'''

    def __init__(self):
        self.head = None  # 鏈結串列頭部的節點
        self.tail = None  # 鏈結串列尾部的節點

    def add_double_node(self, new_node):
        '''將節點加入鏈結串列'''
        if isinstance(new_node, Node):  # 先確認此item是否為節點
            if self.head == None:  # 處理雙向鏈結串列是空的
                self.head = new_node  # 頭是new_node
                new_node.previous = None  # 指向前方
                new_node.next = None  # 指向後方
                self.tail = new_node  # 尾節點也是new_node
            else:  # 處理雙向鏈結串列不是空的
                self.tail.next = new_node  # 尾節點指標指向new_node
                new_node.previous = self.tail  # 新節點前方指標指向前
                self.tail = new_node  # 新節點成為尾部節點
        return

    def print_list_from_head(self):
        '''從頭部列印鏈結串列'''
        ptr = self.head  # 指標指向鏈結串列第1個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def print_list_from_tail(self):
        '''從尾部列印鏈結串列'''
        ptr = self.tail  # 指標指向鏈結串列尾部節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.previous  # 移動指標到前一個節點


double_link = Double_linked_list()
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)

for n in [n1, n2, n3]:
    double_link.add_double_node(n)
    print("從頭部列印雙向鏈結串列")
    double_link.print_list_from_head()  # 從頭部列印雙向鏈結串列

print("從尾部列印雙向鏈結串列")
double_link.print_list_from_tail()  # 從尾部列印雙向鏈結串列

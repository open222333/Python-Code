class Node():
    def __init__(self, data=None) -> None:
        self.data = data  # 資料
        self.next = None  # 指標


class Linked_list():
    def __init__(self) -> None:
        self.head = None  # 鏈結串列的第一個節點

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def search_data(self, *args):
        '''搜尋 數字出現次數'''
        ans = {}
        ptr = self.head
        while ptr:
            if ptr.data not in ans:
                ans[ptr.data] = 1
            else:
                ans[ptr.data] += 1
            ptr = ptr.next
        str_num = ''
        for i in range(len(args)):
            if i != (len(args) - 1):
                str_num += str(args[i]) + ', '
            else:
                str_num += str(args[i])
        print(f"分別列出數值{str_num}的出現次數")
        for target in args:
            if target in ans:
                print(f"{target} 出現 {ans[target]} 次")
            else:
                print(f"{target} 出現 0 次")


link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(5)
link.head.next = n2
n2.next = n3
link.print_list()
link.search_data(5, 15, 20)

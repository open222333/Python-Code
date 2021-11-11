class Node():
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.previous = None


class Linked_list():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

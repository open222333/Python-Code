# 合併兩個已排序的linked list,並排序
# Merge two sorted linked lists and return it as a sorted list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

    # iteratively
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # If you just use one (like cur) how can you return,
        # due to the fact that cur is not pointing to the head any more.
        # you need to store head pointer to return so that's why we use dummy (because cur is traversing ).
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

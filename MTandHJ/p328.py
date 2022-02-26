

from typing import List

from base import version



class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:

    @version("68ms, 19mb")
    def oddEvenList(self, head: ListNode) -> ListNode:
        def split(head):
            if head is None or head.next is None: return head, None
            cur, nxt = head, head.next
            left, right = split(nxt.next)
            cur.next, nxt.next = left, right
            return cur, nxt
        if head is None: return head
        left, right = split(head)
        node = left
        while node.next:
            node = node.next
        node.next = right
        return left
        
    @version("52ms, 16.9mb")
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: return head
        evenhead = head.next
        odd, even = head, evenhead
        while even and even.next:
            odd.next = even.next
            even.next = odd.next
        odd.next = evenhead
        return head
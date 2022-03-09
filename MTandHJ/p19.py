

from typing import List

from attr import Attribute

from base import version



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @version("36ms, 14,9mb")
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def order(head, n):
            if head is None: 
                return head, 1
            newhead, mark = order(head.next, n)
            if mark == n:
                head = newhead
            else:
                head.next = newhead
            return head, mark + 1
        return order(head, n)[0]


    @version("52ms, 14.8mb")
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first, second = head, head
        try:
            for _ in range(n + 1):
                first = first.next
        except AttributeError:
            return head.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
        
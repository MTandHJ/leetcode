

from typing import List, tuple
from typing_extensions import TypeAlias


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverse(self, head: ListNode, tail: ListNode) -> tuple[ListNode]:
        prev = tail.next
        p = head 
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            next = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = next
            pre = tail
            head = tail.next
        return hair.next
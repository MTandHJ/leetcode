

from typing import List

from base import version



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @version("144ms, 29.9mb")
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA is not None:
            headA.flag = True
            headA = headA.next
        while headB is not None:
            if hasattr(headB, 'flag'):
                return headB
            headB = headB.next
        return None
            
    @version("double nodes: 188ms, 29.9mb")
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while True:
            if node1 is node2:
                return node1
            if node1.next is None:
                node1 = headB
            elif node2.next is None:
                node2 = headA
            else:
                node1, node2 = node1.next, node2.next
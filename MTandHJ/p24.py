

from typing import List

from base import version



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @version("28ms, 14.8mb")
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        try:
            while True:
                cur.val, cur.next.val = cur.next.val, cur.val 
                cur = cur.next.next
        except AttributeError:
            pass
        return head

    @version("36ms, 15mb")
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        cur, nxt = head, head.next
        newhead = self.swapPairs(nxt.next)
        cur.next = newhead
        nxt.next = cur
        return nxt

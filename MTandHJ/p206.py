

from typing import List


from base import version



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @version("44ms, 16mb")
    def reverseList(self, head: ListNode) -> ListNode:
        prevs, cur = None, head
        while cur is not None:
            cur.next, cur, prevs = prevs, cur.next, cur

        
    @version("44ms, 20.7mb")
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead

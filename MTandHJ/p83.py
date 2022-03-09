

from typing import List

from base import version



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @version("32ms, 14.9mb")
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        newhead = self.deleteDuplicates(head.next)
        if head.val != newhead.val:
            head.next = newhead
            return head
        else:
            return newhead
            

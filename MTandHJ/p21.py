

from typing import List, Optional

from base import version



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @version("48ms, 15.1mb")
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1
        if list1.val < list2.val:
            newlist = self.mergeTwoLists(list1.next, list2)
            list1.next = newlist
            return list1
        else:
            newlist = self.mergeTwoLists(list1, list2.next)
            list2.next = newlist
            return list2

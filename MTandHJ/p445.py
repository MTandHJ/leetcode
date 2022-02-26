

from typing import List

from base import version



class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:

    @version("52ms, 14.9mb")
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        l = None
        for t in str(num1 + num2)[::-1]:
            l = ListNode(int(t), l)
        return l

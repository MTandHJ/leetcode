

from typing import List
class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val 
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(0)
        cur = pre
        carry = 0
        while l1 or l2:
            x = 0 if not l1 else l1.val
            y = 0 if not l2 else l2.val

            sum = x + y + carry

            carry = sum // 10
            sum = sum  % 10
            cur.next = ListNode(sum)

            if l1:
              l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == 1:
            cur.next = ListNode(carry)
        return pre.next  



from typing import List
from base import version


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @version("hahaha")
    def hasCycle(self, head: ListNode) -> bool:
        try:
            for _ in range(10 ** 4):
                head = head.next
        except AttributeError:
            return False
        return True

    @version("hash")
    def hasCycle(self, head: ListNode) -> bool:
        trajectory = {head}
        try:
            while True:
                head = head.next
                if head in trajectory:
                    return True
                trajectory.add(head)
        except AttributeError:
            return False

    @version("double, slow and fast nodes")
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        try:
            while True:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
        except AttributeError:
            return False

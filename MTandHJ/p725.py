

from typing import List

from base import version



class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:

    @version("44ms, 15.3mb")
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        splits = [length // k] * k
        for i in range(length % k):
            splits[i] += 1
        ans = []
        for split in splits:
            ans.append(head)
            for _ in range(split - 1):
                head = head.next
            try:
                head.next, head = None, head.next
            except AttributeError:
                pass
        return ans

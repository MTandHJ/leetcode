from typing import List

class ListNode:
    def __init__(self, val) -> None:
        self.x = val
        self.next = next

# 直接计算
class Solution:
    def middleNode(self, head: ListNode):
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        
        cur = head
        for i in range(cnt // 2):
            cur = cur.next        
        return cur

# 快慢指针
class Solution:
    def middleNode(self, head: ListNode):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### hash表
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 使用hash表
        visited = set()
        cur = head
        while cur:
            if cur not in visited:
                visited.add(cur)
                cur = cur.next
            else:
                return cur

### 快慢指针
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 使用快慢链表
        # 当只有一个节点时
        if head is None:
            return

        # 初始化
        fast = head
        slow = head

        # 使用快慢指针往后走
        while fast is not None:
            # 找是否有环
            slow = slow.next
            # 当只有一个节点
            if fast.next is not None:
                fast = fast.next.next
            else:
                return
            
            # 找环的入口在哪里
            if fast == slow:
                pred = head
                while pred != slow:
                    pred = pred.next
                    slow = slow.next
                return pred
        return
            
        
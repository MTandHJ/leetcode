

class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None

class Solution:
    def deleteNode(self, head: Node, val: int) -> Node:
        # 防止头节点是空的
        if not head:
            return

        slow, fast = head, head.next
        # 单向链表，所以需要有一个前后指针来标志
        while slow and fast:
            # 防止第一个是待删除的目标节点
            if slow.val == val:
                head = fast
            elif fast.val == val:
                slow.next = fast.next
            
            slow = slow.next
            fast = fast.next
        
        return head

class Solution:
    def deleteNode(self, head:Node, val:int) -> Node:
        if not head:
            return 
        
        if head.val == val:
            return head.next
        
        cur = head
        # 循环到末尾，或者循环到cur，此时cur.next是我们的目标删除值
        while cur.next and cur.next.val != val:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
        
        return head
        
        

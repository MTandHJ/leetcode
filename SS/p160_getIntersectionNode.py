"""编写一个程序，找到两个单链表相交的起始节点。"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:        
        hashset = set()
        cur = headA
        while cur is not None:
            hashset.add(cur)
            cur = cur.next
        
        cur = headB
        while cur is not None:
            if cur in hashset:
                return cur
            cur = cur.next
        return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        # 每个链表走上两个链表嫁接出来的一条路
        # 当走到第二部分时候
        # 若重合，则退出，这个重合的点为我们第一次相交的点，后面都是相交的点
        # 若不重合，两条路合并起来和走到了尽头，都是None，则没有相交的结点。
        while pA != pB:
            if pA is not None:
                pA = pA.next
            else:
                pA = headB
            if pB is not None:
                pB = pB.next
            else:
                pB = headA
        
        return pA
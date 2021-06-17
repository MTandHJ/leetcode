# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 递归法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # (a) 判断是否是空的，这是递归的终止条件
        # 这里返回的是不空的
        # 若l1和l2均是空的，则在第一个if时，就返回了l2（这是空的）
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        # (b) 开始进行递归循环
        # 将l1的下一个元素 = l1.next 和剩下的l2相递归
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 迭代法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # (a) 创建哑节点
        dummy = ListNode(-1)
        pred = dummy
        # (b) 开始更新
        while l1 and l2:
            if l1.val < l2.val:
                pred.next = l1
                l1 = l1.next
            else:
                pred.next = l2
                l2 = l2.next
            pred = pred.next
        # (c) 最后一个结点是不为None的结点
        pred.next = l1 if l1 is not None else l2
        
        # (d) 返回头节点
        return dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # (a) 创建一个哑节点
        dummy = ListNode(0, head)

        # (b) 快慢指针
        slow = dummy
        fast = head

        # (c) 当快指针不为空的时候
        while fast:
            # (1) 更新slow
            # 当检测出来值等于之后
            if fast.val == val:
                # 这里只能是slow跟着fast一起移动
                # slow slow.next slow.next.next
                #      fast      fast.next
                slow.next = fast.next
            else:
                slow = fast
            # (2) 更新fast
            fast = fast.next
        # (d) 返回第一个结点
        return dummy.next
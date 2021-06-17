"""请判断一个链表是否为回文链表。"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(head: ListNode) -> ListNode:
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        # 这是偶数
        # n1    n2  n3  n4 None
        # fast
        # slow
        # n1   n2   n3   n4 None
        #           fast
        #      slow
        # n1   n2   n3   n4 None
        #                   fast
        #           slow

        # n1    n2    n3    n4     n5    None
        # fast
        # slow
        # n1    n2    n3    n4     n5    None
        #             fast
        #       slow
        # n1    n2    n3    n4     n5    None
        #                          fast
        #             slow
        # 这里slow指针就要往后面移动一位：下面情况
        if fast is not None:
            slow = slow.next
        
        # 逆转后半部分的链表
        slow = reverseList(slow)

        fast = head
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True
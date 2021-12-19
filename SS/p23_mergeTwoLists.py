

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, a: ListNode, b: ListNode):
        if not a or not b:
            return a if a else b

        head = ListNode()
        tail = head
        aPtr, bPtr = a, b
        while aPtr and bPtr:
            if aPtr.val < bPtr.val:
                tail.next = aPtr
                aPtr = aPtr.next
            else:
                tail.next = bPtr
                bPtr = bPtr.next
            tail = tail.next
        tail.next = aPtr if aPtr else bPtr
        return head.next
    
    def mergeKLists(self, lists: ListNode[ListNode]):
        ans = None
        for head in lists:
            ans = self.mergeTwoLists(ans, head)
        return ans

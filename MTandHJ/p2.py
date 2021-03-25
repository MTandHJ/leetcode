

from base import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    l1 = [2,4,3], l2=[5,6,4] => [7, 0, 8]
    l1 = [0], l2=[0] => [0]
    l1 = [9, 9], l2=[9] => [8, 0, 1]
    """
    @version("trivial: 72ms, 14.9mb")
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def yieldVal(node1, node2):
            flag1 = False
            flag2 = False
            while True:
                try:
                    val1 = node1.val
                    node1 = node1.next
                except AttributeError:
                    val1 = 0
                    flag1 = True
                try:
                    val2 = node2.val
                    node2 = node2.next
                except AttributeError:
                    val2 = 0
                    flag2 = True
                if flag1 and flag2:
                    break
                yield val1 + val2

        l = yieldVal(l1, l2)
        val = next(l)
        summation = ListNode(val % 10)
        l3 = summation
        while True:
            try:
                val = next(l) + val // 10
                l3.next = ListNode(val % 10)
                l3 = l3.next
            except StopIteration:
                val = val // 10
                if val != 0:
                    l3.next = ListNode(val)
                return summation
        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()

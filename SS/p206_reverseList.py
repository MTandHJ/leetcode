# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 双指针
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # (a) 初始化指针结点
        pre = None
        cur = head

        # (b) 开始迭代
        # pre：我反转之后的结点，从None开始
        # cur：遍历原来的链表，将其中的元素传递给pre, pre用其来反转
        while cur:
            # 记录下cur的下一个元素
            tmp = cur.next
            # 将cur的下一个指针指向pre，这是第一次逆序（单元逆序）
            cur.next = pre
            # pre结点往后走
            # 要先记录pre结点，因为如果不这样的话，先开始cur, 之前的那个前驱结点就没了
            pre = cur
            # cur结点往后走
            cur = tmp

        # (c) 返回逆序的结点
        return pre

# 使用递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # (a) 最后终止条件
        if head is None or head.next is None:
            return head
        # (b) 假设之前的已经反转完
        ret = self.reverseList(head.next)
        # (c) 子单元反转
        # 反转一个结点
        # head -> head.next
        # 反转之后： head <- head.next
        # how to reverse? 下面的
        head.next.next = head
        # 头节点的下一个结点变成了空的
        # 第一个结点的下一个结点是None，不搞这个，最后会进入死循环
        # (d) 最原始的head，是None
        head.next = None

        return ret

    # ret = reverseList(8)
        # 执行：reverseList(6)
            # 执行：reverseList(9)
            #     有返回 返回9
        #   ret = node(9) 
        #   6.next.next = 6 相当于是
        #   6 -> 9（6.next)  变成 6 <- 9 
        #   head.next = None None <- 6 <- 9
        #   此时返回 ret(9)
    # ret = ret(9)
    # 未处理之前：8 -> 6（8.next) None <- 6 <- 9
    # head.next.next = head <=> 6(8.next).next = 8(head) <=> 8 <- 6
    # head.next = None <=> 8(head).next = None



class ListNode:
    def __init__(self, x, next=None) -> None:
        self.x = x
        self.next = next


class Solution:
    def reverse(self, head: ListNode):
        if head is None:
            return head
        # 递归之后的尾部结点
        last = self.reverse(head.next)
        # 1(head) -> None, 2 <- 3 <- 4 <- 5 <- 6(last)
        head.next.next = head
        # None <- 1(head) <- 2 <- 3 <- 4 <- 5 <- 6(last)
        head.next = None
        return last

    # 反转前N个结点
    def reverseN(self, head:ListNode, n: int):
        # 1(head) -> 2 -> 3 -> 4 -> 5 -> 6 -> None
        # reverse(head, 3)
        # 1(head) <- 2 <- 3    4(successor) -> 5 -> 6 -> None
        successor = ListNode(0)
        def subReverse(head:ListNode, n: int):
            if n == 1:
                # 记录 n + 1个结点
                successor = head.next
            # 以head.next 为起点，需要反转前 n - 1 个结点
            last = subReverse(head.next, n-1)
            head.next.next = head
            # 将反转之后的前N个结点和后面的结点连接起来
            head.next = successor
            return last
        return subReverse(head, n)

    def reverseBetween(self, head:ListNode, m:int, n: int):
        if n == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head
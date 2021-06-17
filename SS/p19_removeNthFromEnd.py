
"""19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。"""
# 最简单：计算链表常速
# 亮点：处理链表的头部被删除，加上了一个“哑节点”

class ListNode:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # (a) 获取链表的长度
        def get_len(head:ListNode) -> int:
            cnt = 0
            while head is not None:
                cnt += 1
                head = head.next
            return cnt
        
        # 获取长度，找到被删除的点：找到位置
        # TODO：若n> len怎么办？
        # 我的想法：什么都不做
        length = get_len(head)

        if n > length:
            return

        # (b) 添加哑节点
        dummy = ListNode(0, None)
        cur = dummy
        # (c) 将哑节点与之前的head建立起联系
        cur.next = head
        # (d) 找到被删除节点的前驱节点
        for _ in range(length - n):
            cur = cur.next

        # (e) 删除节点
        cur.next = cur.next.next
        return dummy.next

# 使用栈，先进先出
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # (a) 创建一个哑节点
        dummy = ListNode(0, head)

        # (b) 创建栈，来存放我们的结点
        stack = list()
        cur = dummy
        while cur:
            # 注意：一定要将之前的dummy也添加上去
            stack.append(cur)
            cur = cur.next
        
        # (c) 删除最后的n个结点，stack最后一个节点，就是待删除结点的前驱结点
        for _ in range(n):
            stack.pop()
        # (d) 找到待删除元素的前驱结点，删除
        prev = stack[-1]
        prev.next = prev.next.next

        return dummy.next

# 使用快慢指针，准确来说，是先后指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # (a) 创建一个哑节点
        dummy = ListNode(0, head)

        # (b) 创建快慢指针
        fast = head
        slow = dummy

        # (c) 使得快慢指针之间的距离为n个结点，则两个结点结点距离相差n + 1
        # 这里的slow结点，最后停在待删除结点的前驱结点
        for _ in range(n):
            fast = fast.next
        
        # (d) 当fast到达最后的None时，slow结点到达待删除结点的前驱结点
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # (e) 删除结点
        slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    ins = Solution()
    head = 
"""
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 当为空结点，或者只有一个节点
        if not head or not head.next:
            return False
        
        # 首先设定fast第一次就比slow的快上一步
        fast = head.next
        slow = head
        
        # 当不是环的时候就向前走
        while fast != slow:
            # 当环变成了最后一个时，或者是倒数第一个时，则结束
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
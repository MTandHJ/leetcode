"""p328.py
奇偶链表
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/odd-even-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # (a) 当是空结点时，返回
        if head is None:
            return head

        # (b) 同时创建两个链条，一个偶数，一个奇数
        evenhead = head.next
        odd = head
        even = evenhead

        # (c) 偶数结点和偶数结点的后驱结点，是非空的话，则
        # 开始同时 更新两个链条
        while even is not None and even.next is not None:
            # 这样前一个依赖于一个新创建的even，就更新了
            # 但是odd.next = odd.next.next就不更新？而且可能出现Nonetype等错误
            odd.next = even.next
            # odd更新完毕，指针向后移（移到的这个指针是上一步更新后的
            odd = odd.next

            # 同样方式，更新even
            # 必须要先更新odd，再更新even
            # 因为odd再even前面，我需要讲even的值传给odd
            even.next = odd.next
            even = even.next

        # (e) 连接两个链表
        odd.next = evenhead
        return head
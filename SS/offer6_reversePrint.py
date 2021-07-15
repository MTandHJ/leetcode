
from typing import List
class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val 
        self.next = next

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = list()
        temp = head
        while not temp:
            stack.append(temp)
            temp = temp.next
        
        size = len(stack)
        pri = []
        for i in range(size):
            pri[i] = stack.pop().val

        return pri
from p206_reverseList import ListNode
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        def helper(start: int):
            # 基本情况：到了元素的最后一个位置
            # 迭代需要停止了
            if start == n:
                return
            # 找到这个位置
            c = s[start]
            helper(start + 1)
            s[n - 1 - start] = c
        helper(0)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def subReverse(s, i, j):
            if i >= j:
                return s
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            return subReverse(s, i, j)
        return subReverse(s, 0, len(s) -1)

    def reverseString2(self, s):
        def subReverse(s, i, j):
            if i >= j:
                return s
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            subReverse(s, i, j)
        subReverse(s, 0, len(s)-1)
        return s


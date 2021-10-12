


from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            # 如果当前的能够满足，则分别向后移动
            # 两个都动，继续找下一个满足的
            if s[j] >= g[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res
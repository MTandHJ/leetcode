

from base import version

class Solution:

    def countBinarySubstrings(self, s: str) -> int:
        s = s + '$'
        ans = x = y = 0
        for left in range(len(s) - 1):
            y += 1
            if s[left] != s[left + 1]:
                ans += min(x, y)
                x, y = y, 0
        return ans

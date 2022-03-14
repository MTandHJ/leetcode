

import collections

from base import version

class Solution:

    def longestPalindrome(self, s: str) -> int:
        counts = collections.defaultdict(int)
        for item in s:
            counts[item] += 1
        ans = 0
        for val in counts.values():
            ans += val // 2
        ans *= 2
        ans = ans if len(s) == ans else ans + 1
        return ans
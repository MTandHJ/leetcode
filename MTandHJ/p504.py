

from typing import List

from base import version

import math

class Solution:

    def findMaxBase(self, num):
        base = -1
        steps = -1
        while base <= num:
            steps += 1
            base = 7 ** steps
        return steps - 1

    @version("40ms, 14.9mb")
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        ans = '-' if num < 0 else ''
        num = abs(num)
        MaxBase = int(self.findMaxBase(num))
        for base in range(MaxBase, -1, -1):
            base = 7 ** base
            ans += str(num // base)
            num = num % base
        return ans
            

test = Solution().convertToBase7(100)
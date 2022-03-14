

from typing import List

from base import version

class Solution:

    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        ans = 0
        while z:
            ans += 1
            z = z & (z - 1)
        return ans
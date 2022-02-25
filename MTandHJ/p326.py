

from typing import List

from base import version


class Solution:

    @version("68ms, 14.8mb")
    def isPowerOfThree(self, n: int) -> bool:
        ans = 1
        while ans < n:
            ans *= 3
        return ans == n
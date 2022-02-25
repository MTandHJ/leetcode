

from typing import List

from base import version


class Solution:

    @version("40ms, 14.9mb")
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n > 0:
            n = n // 5
            ans += n
        return ans



from typing import List

from base import version


class Solution:

    @version("56ms, 15mb")
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            pow_ = m * m
            if pow_ == x:
                return m
            elif pow_ > x:
                r = m - 1
            else:
                l = m + 1
        return r

    @version("36ms, 15mb")
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            m = l + (r - l) // 2
            pow_ = m * m
            if pow_ >= x:
                r = m
            else:
                l = m + 1
        if r * r == x:
            return r
        else:
            return r - 1
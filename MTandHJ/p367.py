

from typing import List

from eagerpy import square

from base import version


class Solution:

    @version("80ms, 14.8mb")
    def isPerfectSquare(self, num: int) -> bool:
        ans = 1
        while ans ** 2 < num:
            ans += 1
        return ans ** 2 == num


    @version("48ms, 70.30")
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left < right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            else:
                right = mid
        return (left * right) == num

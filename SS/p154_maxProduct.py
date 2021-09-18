

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax = 1
        imin = 1
        res = max(nums)
        for i in nums:
            if i > 0:
                imax = max(i, imax*i)
                imin = min(i, imin*i)
            else:
                temp = imax
                imax = max(i, imin*i)
                imin = min(i, temp*i)
            res = max(res, imax)
        return res
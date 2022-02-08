

from typing import List

from base import version


class Solution:

    @version("24ms, 15mb")
    def rob(self, nums: List[int]) -> int:
        x, y = 0, nums[0]
        a, b = 0, 0
        for i in range(1, len(nums) - 1):
            x, y = y, max(y, x + nums[i])
            a, b = b, max(b, a + nums[i])
        return max(y, a + nums[-1])
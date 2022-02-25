

from typing import List

from base import version


class Solution:

    @version("72ms, 15.7mb")
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


from typing import List

from base import version

class Solution:

    @version("56ms, 15.9mb")
    def missingNumber(self, nums: List[int]) -> int:
        nums = nums + [k for k in range(len(nums) + 1)]
        return reduce(lambda x, y: x ^ y, nums)

    @version("44ms, 16.9mb")
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = set(range(len(nums) + 1)) - nums
        return nums.pop()


from typing import List

from base import version


class Solution:

    @version("over time limits")
    def rob(self, nums: List[int]) -> int:
        def search(nums):
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums)
            return max(search(nums[:-1]), search(nums[:-2]) + nums[-1])
        return search(nums)

    @version("36ms, 15.1mb")
    def rob(self, nums: List[int]) -> int:
        memory = {0: 0, 1: nums[1]}
        def search(n):
            if memory.get(n, None) is None:
                memory[n] = max(search(n - 1), search(n - 2) + nums[n - 1])
            return memory[n]
        return search(len(nums))

    @version("24ms, 15.1mb")
    def rob(self, nums: List[int]) -> int:
        x, y = 0, nums[0]
        for i in range(1, len(nums)):
            x, y = y, max(y, x + nums[i])
        return y



from typing import List

from base import version


class Solution:

    @version("36ms, 20.8mb")
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        memory = {0:0, 1:0}
        def search(n):
            if memory.get(n, None) is None:
                search(n-1)
                if nums[n] - nums[n-1] != nums[n-1] - nums[n-2]:
                    memory[n] = 0
                else:
                    memory[n] = memory[n-1] + 1
            return memory[n]
        search(len(nums) - 1)
        counts = 0
        for value in memory.values():
            counts += value
        return counts

    @version("32ms, 15.2mb")
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        counts, cur = 0, 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] != nums[i-1] - nums[i-2]:
                cur = 0
            else:
                cur += 1
                counts += cur
        return counts

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

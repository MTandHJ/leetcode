

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums or not target:
            return 0
        maximum = [0] * (target + 1)
        maximum[0] = 1
        nums.sort()
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if nums[j] <= i:
                    maximum[i] += maximum[i - nums[j]]
        return maximum[-1]
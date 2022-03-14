

from typing import List

from base import version


class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        idx = 0
        ans = 0
        count = 0
        while idx < len(nums):
            if nums[idx]:
                count += 1
            else:
                ans = max(ans, count)
                count = 0
            idx += 1
        return max(ans, count)

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = count = 0
        for num in nums:
            if num:
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        return max(ans, count)


from turtle import right
from typing import List

from base import version


class Solution:

    @version("32ms, 16.3mb")
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

    @version("quickSort: over time limits")
    def majorityElement(self, nums: List[int]) -> int:
        def quickSort(nums):
            if len(nums) <= 1: return nums
            anchor = nums[0]
            left, right = [], []
            for num in nums[1:]:
                if num < anchor:
                    left.append(num)
                else:
                    right.append(num)
            return quickSort(left) + [anchor] + quickSort(right)
        return quickSort(nums)[len(nums) // 2]


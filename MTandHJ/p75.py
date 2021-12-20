


from typing import List, Optional, Iterable, Dict
from collections import defaultdict

from base import version

class Solution:

    @version("32ms, 15mb")
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

    @version("32ms, 14.6mb")
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

    @version("single: 32ms, 15mb")
    def sortColors(self, nums: List[int]) -> None:
        head, end = 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                head += 1
        for i in list(range(head, len(nums)))[::-1]:
            if nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1



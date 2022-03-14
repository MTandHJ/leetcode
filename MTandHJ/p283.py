

from typing import List

from base import version


class Solution:

    @version("40ms, 15.9mb")
    def moveZeroes(self, nums: List[int]) -> None:
        left = len(nums)
        for left, num in enumerate(nums):
            if num == 0:
                break
        for right in range(left + 1, len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            
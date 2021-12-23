



from typing import List

from base import version



class Solution:

    @version("32ms, 15.2mb")
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[r]

    @version("24ms, 15mb")
    def findMin(self, nums: List[int]) -> int:
        l, r= 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= nums[-1]:
                r = m
            else:
                l = m + 1
        return nums[r]

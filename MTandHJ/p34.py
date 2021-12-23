


from typing import List

from base import version



class Solution:

    @version("36ms, 15.8mb")
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not len(nums):
            return ans
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        ans[0] = r
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        ans[1] = r - 1
        if ans[0] == len(nums):
            return [-1, -1]
        if nums[ans[0]] == target:
            return ans
        else:
            return [-1, -1]


    @version("28ms, 15.8mb")
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums = [-float('inf')] + nums + [float('inf')]
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        if nums[r] != target:
            return [-1, -1]
        ans = [r-1, r-1]
        l, r = r, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        ans[1] = r - 2
        return ans
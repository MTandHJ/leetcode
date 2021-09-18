
from typing import List


class Solution:
    def searchRange(self, nums, target: int) -> List[int]:
        leftIdx = self.binarySearch(nums, target, True)
        rightIdx = self.binarySearch(nums, target, False)
        if leftIdx <= rightIdx and rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target:
            return leftIdx, rightIdx
        
        return -1, -1
    
    def binarySearch(self, nums: List[int], target: int, lower: bool):
        left, right = 0, len(nums) -1
        ans = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        
        return ans
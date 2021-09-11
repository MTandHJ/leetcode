
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]):
        return self.search(nums, 0, len(nums) - 1))
    
    def search(self, nums: List[int], l: int, r: int):
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            # 左边是上升的，可能就在左边
            self.search(nums, l, mid)
        # 右边就是上升的，可能就在右边
        return self.search(nums, mid + 1, r)

    def search_2(self, nums: List[int]):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = ( l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
from typing import List

class Solution:
    def search(self, nums: List[int], target: int):
        n = len(nums)
        if n == 0:
            return False
        if n == 1:
            return nums[0] == target
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # 1, 一条直线
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            # 2, 左边是完整的斜线
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    # 为什么是mid + 1
                    # 因为左边是升序的，但是target并不在左边的区间里面，
                    l = mid + 1
            else:
                # 3, 右边是完整的斜线
                if nums[mid] < target and target <= nums[n-1]:
                    # 这是说目标在右边
                    l = mid + 1
                else:
                    # TODO： 没弄明白
                    r = mid - 1
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        
        n = len(nums)
        i, j, k = n - 2, n- 1, n - 1
        # 找nums[i] < nums[j]的
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        # 在[j, end)中找 k, st. A[i] < A[k]
        # k 是第一个满足条件的索引
        while i >= 0:
            # 不满足条件就减减
            if nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]

        # 最后反转[j, end)
        end = n - 1
        while j < end:
            nums[j], nums[end] = nums[end], nums[j]
            j += 1
            end -= 1
        

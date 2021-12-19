

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if not nums:
            return 1
        n = len(nums)
        # 将所有负数置换为n + 1（之后变换不再考虑）
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # 找到在[1, N]中的数, 并且标记
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        # 找到第一个在[1, N]中的正数，
        # 这个“下标”位置是我们要找的正数
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

            


from typing import List

from base import version


class Solution:

    @version("over time limits")
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = 1
        for i in range(len(nums)):
            for j in range(i):
                nums[j] *= nums[i]
            nums[i], tmp = tmp, nums[i] * tmp
        return nums

    @version("76ms, 22.8mb")
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L, R = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i - 1]
            R[-i-1] = R[-i] * nums[-i]
        return [l * r for l, r in zip(L, R)]

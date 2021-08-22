

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List) -> int:
        n = len(nums)

        max_ = -float('INF')
        pre = 0
        for i in range(n):
            pre = nums[i] + max(pre, 0)
            max_ = max(max_, pre)

        if max_ < 0:
            return max_

        pre = 0
        min_ = float('INF')
        for i in range(n):
            pre = min(0, pre) + nums[i]
            min_ = min(min_, pre)

        return max(max_, sum(nums) - min_)
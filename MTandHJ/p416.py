

from typing import List

from base import version


class Solution:

    @version("dp: 5476ms, 44.9mb")
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        if n % 2 != 0:
            return False
        m = len(nums)
        n = n // 2
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                v = nums[i - 1]
                nxt = dp[i - 1][max(j - v, 0)] + v
                nxt = -1 if nxt > j else nxt
                dp[i][j] = max(dp[i - 1][j], nxt)
        return dp[m][n] == n

    @version("dp: 5396ms, 15.3mb")
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        if n % 2 != 0:
            return False
        m = len(nums)
        n = n // 2
        dp = [0 for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                v = nums[i - 1]
                nxt = dp[max(j - v, 0)] + v
                nxt = -1 if nxt > j else nxt
                dp[j] = max(dp[j], nxt)
        return dp[-1] == n


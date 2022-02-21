

from typing import List

from base import version




class Solution:

    @version("dp: 2448ms, 15.2mb")
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp1 = [0 for _ in range(days + 1)]
        dp2 = [0 for _ in range(days + 1)]
        for i in range(1, days + 1):
            dp1[i] = dp1[i - 1]
            dp2[i] = dp1[i - 1]
            for j in range(1, i):
                dp1[i] = max(dp1[i], dp2[j - 1] + prices[i - 1] - prices[j - 1])
        return dp1[-1]

    @version("dp: 2544ms, 15.2mb")
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [0 for _ in range(days + 2)]
        for i in range(2, days + 2):
            dp[i] = dp[i - 1]
            for j in range(2, i):
                dp[i] = max(dp[i], dp[j - 2] + prices[i - 2] - prices[j - 2])
        return dp[-1]

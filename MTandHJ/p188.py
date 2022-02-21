

from typing import List

from base import version




class Solution:

    @version("dp: 88ms, 14.9mb")
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days == 0:
            return 0
        dp = [0 for _ in range(k + 1)]
        prevs = [-prices[0] for _ in range(k)]
        for i in range(days):
            for j in range(k, 0, -1):
                dp[j] = max(dp[j], prices[i] + prevs[j - 1])
                prevs[j - 1] = max(prevs[j - 1], dp[j - 1] - prices[i])
        return dp[-1]

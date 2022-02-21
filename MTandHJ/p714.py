

from typing import List

from base import version




class Solution:

    @version("dp: 288ms, 20.8mb")
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        dp = [0 for _ in range(days + 1)] 
        the_max = dp[0] - prices[0]
        for i in range(1, days + 1):
            dp[i] = max(dp[i - 1], the_max + prices[i - 1] - fee)
            the_max = max(the_max, dp[i - 1] - prices[i - 1])
        return dp[-1]
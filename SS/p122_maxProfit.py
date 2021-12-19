

from typing import List


class Solution:
    # 贪心算法
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        buy = max(-float('inf'), -prices[0])
        sell = max(0, prices[0] + buy)

        for p in prices[1:]:
            buy = max(buy, sell - p)
            sell = max(sell, p - buy)
        return sell
    
    # 动态规划：二维数组
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return max(dp[-1])

    # 将二维数组变成一维数组
    def maxProfit3(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [0] * 2
        dp[1] = -prices[0]
        for i in range(1, n):
            dp[0] = max(dp[0], dp[1] + prices[i])
            dp[1] = max(dp[0] - prices[i], dp[1])
        return max(dp)

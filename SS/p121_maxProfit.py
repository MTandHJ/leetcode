
# 1. 找最小值，2. 找与最小值之差最大的最大值
# NOTE: 一定要从前面往后遍历, 因为买股票只能在买股票后面
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_prices = max(prices) + 1
        # min_prices = float('inf') # 也是可以的
        for i in range(len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]
            elif prices[i] - min_prices > max_profit:
                max_profit = prices[i] - min_prices
        
        return max_profit
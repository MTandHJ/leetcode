
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_prices = max(prices) + 1
        for i in range(len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]
            elif prices[i] - min_prices > max_profit:
                max_profit = prices[i] - min_prices
        
        return max_profit
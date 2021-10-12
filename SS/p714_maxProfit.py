
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee) -> int:
        if not prices:
            return 0
        n = len(prices)
        f0, f1 = -prices[0] - fee, 0
        for i in range(1, n):
            newf0 = max(f0, f1 - prices[i] - fee)
            newf1 = max(f0 + prices[i], f1)
            f0, f1 = newf0, newf1
        return max(f0, f1)
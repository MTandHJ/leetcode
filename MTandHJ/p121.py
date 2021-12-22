


from typing import List

from base import version


class Solution:

    @version("96ms, 22.8mb")
    def maxProfit(self, prices: List[int]) -> int:
        bottom, top = prices[0], prices[0]
        wealth = []
        for price in prices:
            if price < bottom:
                wealth.append(top - bottom)
                bottom = price
                top = price
            elif price > top:
                top = price
        wealth.append(top - bottom)
        return max(wealth)



from typing import List

from base import version


class Solution:

    @version("40ms, 15.7mb")
    def maxProfit(self, prices: List[int]) -> int:
        bottom, top = prices[0], prices[0]
        wealth = []
        for price in prices:
            if price < top:
                wealth.append(top - bottom)
                bottom = price
                top = price
            else:
                top = price
        wealth.append(top - bottom)
        return sum(wealth)

    @version("40ms, 15.7mb")
    def maxProfit(self, prices: List[int]) -> int:
        prices = [prices[0]] + prices + [prices[-1]]
        profit = 0
        for cur, nxt in zip(prices[:-1], prices[1:]):
            profit += max(nxt - cur, 0)
        return profit
            
    @version("44ms, 15.7mb")
    def maxProfit(self, prices: List[int]) -> int:
        prices = [prices[0]] + prices + [prices[-1]]
        profits = [max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1)]
        return sum(profits)





from typing import List

from base import version




class Solution:

    @version("dp: 808ms, 27.8mb")
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dps = [[0] * (days + 1) for _ in range(3)]
        the_max = [-prices[0], -prices[0]]
        for i in range(1, days + 1):
            for k in range(2, 0, -1):
                dps[k][i] = max(dps[k][i - 1], the_max[k - 1] + prices[i - 1])
                the_max[k - 1] = max(the_max[k - 1], dps[k - 1][i - 1] - prices[i - 1])
        return dps[2][-1]
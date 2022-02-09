

from typing import List

from base import version


class Solution:


    @version("dp: 7036ms, 25.4mb")
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        for i in range(1, amount + 1):
            for j in range(1, len(coins) + 1):
                if i >= coins[j - 1]:
                    dp[j][i] += sum([dp[k][i - coins[j - 1]] for k in range(j + 1)])
        return sum([dp[j][-1] for j in range(len(coins) + 1)])


    @version("dp: 116ms, 15.1mb")
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]

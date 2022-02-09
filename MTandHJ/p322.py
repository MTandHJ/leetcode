

from typing import List

from base import version


class Solution:

    @version("over time limits")
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        prev_node = [0]
        prev_idx = [0]
        steps = 0
        while len(prev_node) > 0:
            # print(prev_node)
            print(min(prev_node), max(prev_node), len(prev_node))
            steps += 1
            nxt_node = []
            nxt_idx = []
            for i, node in enumerate(prev_node):
                for j, coin in enumerate(coins[prev_idx[i]:], prev_idx[i]):
                    value = node + coin
                    if value == amount:
                        return steps
                    elif value < amount:
                        nxt_node.append(value)
                        nxt_idx.append(j)
            prev_node = nxt_node
            prev_idx = nxt_idx
        return -1

    @version("dp: 1336ms, 15.3mb")
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]

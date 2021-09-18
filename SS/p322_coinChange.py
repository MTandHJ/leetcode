
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]

            res = float('INF')
            if n < 0:
                return -1
            if n == 0:
                return 0
            for coin in coins:
                # 后来需要使用dp[n-coin] 因为之前判断过
                subproblem = dp[n - coin]
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        
        dp(amount)
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return -1 if dp[amount] == amount + 1 else dp[amount]
            
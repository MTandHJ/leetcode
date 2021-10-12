
from typing import List
import functools

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or not coins:
            return 0
        dp = [0] * (amount + 1)
        for coin in coins:
            for i in coin(coin, amount + 1):
                if i == coins:
                    dp[i] = 1
                elif dp[i] == 0 and dp[i-coin] != 0:
                    dp[i] = dp[i-coin] + 1
                elif dp[i - coin] != 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return -1 if dp[amount] == 0 else dp[amount]
    
    def coinChange2(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem) -> int:
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            mini = int(1e9)
            for coin in coins:
                # 当有一种情况可以凑成的时候
                res = dp(rem-coin)
                # 当前为0
                if res >= 0 and res < mini:
                    mini = res + 1
                return mini if mini < int(1e9) else -1
        if amount < 1:
            return 0
        return dp(amount)
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        

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
            

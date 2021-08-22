from typing import List

class Solution:
    def coinChange(self, coins:List[int], amount: int) -> int:
        # 最优子结构，子问题间必须相互独立
        if amount == 0:
            return 0
        # 我们都是正数，没有办法凑齐负数
        if amount < 0:
            return -1
        def dp(n):
            # 在这个函数刚开始初始化res
            res = float('inf')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1:
                    continue
                # 当前硬币被列入凑数范围
                res = min(res, 1 + subproblem)
            return -1 if res == float('inf') else res
        
        return dp(amount)

# 天界备忘录memo的
class Solution:
    def coinChange(self, coins:List[int], amount: int) -> int:
        # 最优子结构，子问题间必须相互独立
        if amount == 0:
            return 0
        # 我们都是正数，没有办法凑齐负数
        if amount < 0:
            return -1
        memo = dict()
        def dp(n):
            if n in memo:
                return memo[n]
            # 在这个函数刚开始初始化res
            res = float('inf')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1:
                    continue
                # 当前硬币被列入凑数范围
                res = min(res, 1 + subproblem)

            memo[n] = -1 if res == float('inf') else res
            # 这点跟fib消除重叠子问题很像啊
            # 1，搞一个列表或者dict当作备忘
            # 2，在子函数计算末尾（return）之前，更新memo
            # 3，最后返回这个更新的memo
            return memo[n]
        
        return dp(amount)
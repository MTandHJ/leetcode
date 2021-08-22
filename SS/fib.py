
from typing import Counter, List

class Solution:
    '''
    1. 重叠子问题 -》 dp数组，备忘录
    状态转移方程
    2. 最优子结构，未涉及
    '''
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        memo = [0] * (n+1)
        return self.helper(memo, n)
    
    def helper(self, memo: List, n:int):
        if n == 1 or n == 2:
            return n
        
        if memo[n]:
            return memo[n]
        # 如果是这样的话，memo[n] 如何更新呢？
        # return self.helper(n-1) + self.helper(n-2)
        # 所以这里需要更新memo
        memo[n] = self.helper(memo, n-1), self.helper(memo, n-2)
        return memo[n]
    
    def fib2(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        
        dp = [0] * (n-1)
        dp[1] = dp[2] = 1
        
        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

        # pre, cur = 1, 1
        # for i in range(3, n):
        #     pre, cur = cur, pre + cur 
        
        # return cur
    
    
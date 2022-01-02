

from typing import List

from base import version


class Solution:

    @version("over time limits")
    def climbStairs(self, n: int) -> int:
        def search(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            ans = 0
            for i in range(2):
                ans += search(n - 1 - i)
            return ans
        return search(n)

    @version("over time limits")
    def climbStairs(self, n: int) -> int:
        def search(n):
            if n == 1 or n == 0:
                return 1
            return search(n - 1) + search(n - 2)
        return search(n)
    
    @version("32ms, 14.9mb")
    def climbStairs(self, n: int) -> int:
        memory = {1:1, 0:1}
        def search(n):
            if memory.get(n, None) is None:
                memory[n] = search(n - 1) + search(n - 2)
            return memory[n]
        return search(n)

    @version("32ms, 14.9mb")
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n-1]

    @version("24ms, 15mb")
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b
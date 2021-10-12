
from typing import List


class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        
        memo = [0] * (n + 1)

        def helper(memo: List[int], n: int):
            if n  == 1 or n == 2:
                return 1
            if memo[n] != 0:
                return memo[n]
            memo[n] = helper(memo, n - 1) + helper(memo, n - 2)
            return memo[n]
        return helper(memo, n)

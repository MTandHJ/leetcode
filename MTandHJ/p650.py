

from typing import List

from base import version


class Solution:

    @version("dp: 216ms, 14.8mb")
    def minSteps(self, n: int) -> int:
        dp = [k for k in range(1, n + 1)]
        dp[0] = 0
        for k in range(1, n + 1):
            for m in range(k // 2 + 1, 0, -1):
                if (k - m) % m == 0:
                    print(m)
                    dp[k - 1] = min(dp[k - 1], dp[m - 1] + (k - m) // m + 1)
                    break
        return dp[-1]
    
test = Solution()
test.minSteps(3)
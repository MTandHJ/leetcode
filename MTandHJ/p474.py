

from typing import List

from base import version


class Solution:

    @version("dp: 4120ms, 15.1mb")
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ones = [item.count('1') for item in strs]        
        zeros = [item.count('0') for item in strs]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(len(strs)):
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j < zeros[i] or k < ones[i]:
                        v = 0
                    else:
                        v = dp[j - zeros[i]][k - ones[i]] + 1
                    dp[j][k] = max(v, dp[j][k])
        return dp[-1][-1]

test = Solution()
test.findMaxForm(['10', '0', '1'], 1, 1)



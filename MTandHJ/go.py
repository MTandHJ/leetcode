


import sys


import collections


class Solution:


    def main(self, probs, k):
        n = len(probs)
        dp = [0] * (k + 2)
        dp[1] = 1
        for i in range(n):
            for j in range(k + 1, 0, -1):
                dp[j] = dp[j] * (1 - probs[i]) + dp[j - 1] * probs[i]
        return dp[-1]


test = Solution()
print(test.main([0.5, 0.5, 0.5, 0.5, 0.5], 3))
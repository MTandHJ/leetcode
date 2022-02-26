

from tkinter import W
from typing import List

from base import version


class Solution:

    @version("dp: 164ms, 23.5mb")
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[i + j for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

    @version("dp: 128ms, 15mb")
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [j for j in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            dp[0] = i - 1
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j], dp[0] = dp[0], dp[j]
                else:
                    dp[j], dp[0] = min(dp[j], dp[j - 1], dp[0]) + 1, dp[j]
            dp[0] = i
        return dp[-1]


test = Solution()
test.minDistance("horse", "ros")
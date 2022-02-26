

from typing import List

from base import version


class Solution:

    @version("dp: 2008ms, 19.1mb")
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = dp[i - 1][j - 1]
                for k in range(j, 0, -1):
                    if word1[i - 1] == word2[k - 1]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k - 1] + 1)
                        break
                for k in range(i, 0, -1):
                    if word1[k - 1] == word2[j - 1]:
                        dp[i][j] = max(dp[i][j], dp[k - 1][j - 1] + 1)
                        break
        return len(word1) + len(word2) - dp[-1][-1] * 2

    @version("dp: 244ms, 17.3mb")
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - dp[-1][-1] * 2


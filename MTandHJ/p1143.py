

from typing import List

from base import version


class Solution:

    @version("dp: 5736ms, 120mb")
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = dict()
        def search(i, j):
            if i < 0 or j < 0:
                return 0
            key = str(i) + ',' + str(j)
            try:
                return dp[key]
            except KeyError:
                if text1[i] == text2[j]:
                    nums = search(i-1, j-1) + 1
                else:
                    nums = max(search(i-1, j), search(i, j-1))
                dp[key] = nums
                return nums
        return search(len(text1) - 1, len(text2) - 1)

    @version("dp: 524ms, 25.2mb")
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[None] * len(text2) for _ in range(len(text1))]
        def search(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] is None:
                if text1[i] == text2[j]:
                    dp[i][j] = search(i-1, j-1) + 1
                else:
                    dp[i][j] = max(search(i-1, j), search(i, j-1))
            return dp[i][j]
        return search(len(text1) - 1, len(text2) - 1)

    @version("dp: 340ms, 22.9mb")
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


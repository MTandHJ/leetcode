

from typing import List

from base import version


class Solution:

    @version("dp: 40ms, 15mb")
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and s[:i][-len(word):] == word:
                    dp[i] += dp[i - len(word)]
        return dp[-1] != 0







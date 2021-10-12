

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> int:
        wordDictSet = dict(wordDict)
        # n = len(s)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDictSet:
                    # 找到一个切分点，使得s[:i]能够成为wordDict的子集
                    dp[i] = True
                    break # 不用再找s[:i]的切分点j了
        return dp[-1]
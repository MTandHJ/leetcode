

from typing import List

from base import version


class Solution:

    @version("greedy: 60ms, 15.3mb")
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda pair: pair[-1])
        right = pairs[0][-1]
        nums = 1
        for pair in pairs[1:]:
            if pair[0] > right:
                nums += 1
                right = pair[-1]
        return nums

    @version("dp: 2176ms, 15.3mb")
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda pair: pair[-1])
        dp = [1] * len(pairs)
        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)








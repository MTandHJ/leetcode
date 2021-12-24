

from typing import List

from base import version


class Solution:

    @version("over time limits")
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        ans = []
        for m in range(1, int(n ** 0.5) + 1):
            ans.append(1 + self.numSquares(n - m ** 2))
        return min(ans)

    def numSquares(self, n: int) -> int:
        candidates = [i for i in range(1, int(n ** 0.5) + 1)]
        depth = 0
        prev = [(0, 0)]
        while True:
            cur = []
            depth += 1
            for start, lst in prev:
                for idx, nxt in enumerate(candidates[start:], start):
                    cum = lst + nxt ** 2
                    if cum == n:
                        return depth
                    elif cum < n:
                        cur.append((idx, cum))
                    else:
                        break
            prev = cur

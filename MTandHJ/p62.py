

from typing import List

from base import version


class Solution:

    @version("28ms, 15.4mb")
    def uniquePaths(self, m: int, n: int) -> int:               
        memory = {(0, 0): 1}
        def search(x, y):
            if memory.get((x, y), None) is None:
                ans = 0
                for l, r in [(-1, 0), (0, -1)]:
                    i, j = x + l, y + r
                    if 0 <= i < m and 0 <= j < n:
                        ans += search(i, j)
                memory[(x, y)] = ans
            return memory[(x, y)]
        return search(m - 1, n - 1)

    @version("28ms, 14.9mb")
    def uniquePaths(self, m: int, n: int) -> int:               
        dps = [0] * (n + 1)
        dps[0] = 1
        for i in range(m):
            for j in range(n):
                dps[j + 1] = dps[j] + dps[j + 1]
            dps[0] = 0
        return dps[-1]







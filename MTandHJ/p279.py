

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

    @version("5452ms, 39.2mb")
    def numSquares(self, n: int) -> int:
        memory = {1:1, 2:2}
        def search(n):
            if memory.get(n, None) is None:
                sqrtn = n ** 0.5
                if int(sqrtn) == sqrtn:
                    memory[n] = 1
                else:
                    ans = float('inf')
                    for i in range(int(sqrtn), 0, -1): # why not for i in range(1, int(sqrtn) + 1): ... ?
                        ans = min(ans, 1 + search(n - i * i))
                    memory[n] = ans
            return memory[n]
        return search(n)
    
    @version("6336ms, 15.2mb")
    def numSquares(self, n: int) -> int:
        dps = [0]
        for i in range(1, n + 1):
            ans = float('inf')
            for j in range(int(i ** 0.5), 0, -1):
                ans = min(ans, 1 + dps[i - j ** 2])
            dps.append(ans)
        return dps[-1]

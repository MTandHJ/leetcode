

from typing import List

from base import version


class Solution:

    @version("40ms, 14.9mb")
    def integerBreak(self, n: int) -> int:
        memory = {1:1, 2:1, 3:2}
        def search(n):
            if memory.get(n, None) is None:
                ans = 0
                for i in range(1, n // 2 + 1):
                    ans = max(
                        ans, 
                        max(i, search(i)) * max(n - i, search(n - i))
                    )
                memory[n] = ans
            return memory[n]
        return search(n)


from typing import List


class Solution:

    def countBits(self, n: int) -> List[int]:
        counts = [0]
        while len(counts) < n:
            counts += [k + 1 for k in counts]
        return counts[:n+1]




from typing import List

from base import version


class Solution:

    @version("220, 15.4mb")
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        depth = -1
        h, w = len(grid) - 1, len(grid[0]) - 1
        prev = [(-1, -1)]
        while prev:
            depth += 1
            cur = []
            if (h, w) in prev:
                return depth
            for (x, y) in prev:
                for (m, n) in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
                    try:
                        assert (x + m) >= 0 and (y + n) >= 0
                        if not grid[x + m][y + n]:
                            cur.append((x + m, y + n))
                            grid[x + m][y + n] = 1
                    except (IndexError, AssertionError):
                        pass
            prev = cur
        return -1

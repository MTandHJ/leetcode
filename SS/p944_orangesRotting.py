

from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        que = deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    que.append((r, c, 0))
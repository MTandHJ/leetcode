

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        depth = 0

        # rotted = [(i, j) for i in range(n) for j in range(m) if grid[i][j]==2]
        que = deque(rotted)
        
        count = 0
        rotted = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotted.append((i, j))
                if grid[i][j] == 1:
                    count += 1
        
        depth = 0
        while que and count > 0:
            depth += 1
            size = len(que)
            for _ in range(size):
                i, j = que.pop()
                for (ni, nj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<= ni < n and 0<=nj < m and grid[ni][nj] == 1:
                        que.push((ni, nj))
                        count -= 1
        
        return depth
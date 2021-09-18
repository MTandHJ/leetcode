
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    a = self.area(grid, r, c)
                    res = max(res, a)
        return res
    
    def area(self, grid, r, c):
        if not self.in_area(grid, r, c):
            return 0
        
        if grid[r][c] != 1:
            return 0
        
        grid[r][c] = 2

        return 1 \
            + self.area(grid, r+1, c) \
                + self.area(grid, r-1, c) \
                    + self.area(grid, r, c+1) \
                        + self.area(grid, r, c-1)
        
    
    def in_area(self, grid, r, c):
        if 0 <= r <len(grid) and 0 <= c < len(grid[0]):
            return True
        
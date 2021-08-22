

from typing import List
class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        def dfs(grid, i, j):
            grid[i][j] = 0
            r, c = len(grid), len(grid[0])
            for di, dj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= di < r and 0 <= dj < c and grid[di][dj] == '1':
                    dfs(grid, di, dj)

        
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        
        return res
        

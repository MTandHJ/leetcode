

from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        que = []

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    que.append((i, j))
        
        time = 0
        while count > 0 and len(que) > 0:
            time += 1
            size = len(que)
            for i in range(size):
                i, j = que.pop(0)
                if i - 1 >=0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    count -= 1
                    que.append((i-1, j))
                if i < n and grid[i][j] == 1:
                    grid[i+1][j] = 2
                    count -= 1
                    que.append((i+1, j))
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    count -= 1
                    que.append((i, j-1))
                if i + 1< m and grid[i][j] == 1:
                    grid[i][j+1] = 2
                    count -= 1
                    que.append((i, j+1))
        
        return -1 if count > 0 else time
                
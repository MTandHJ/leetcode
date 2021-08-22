
# 岛屿最大面积
'''
1.  从某位置出发，向四个方向探寻项链的土地
2. 没探寻到一块土地，计数加一
3. 确保每块土地只会被探寻一次

图的遍历

图的遍历：
DFS, BFS
'''
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def Island(i, j, grid):
            if 0 <= i < len(grid) and 0<= j < len(grid[0]):
                if grid[i][j] == 0:
                    return 0
                else:
                    grid[i][j] = 0
                    left, right = Island(i-1, j, grid), Island(i+1, j, grid)
                    up, down = Island(i, j-1, grid), Island(i, j+1, grid)
                    return 1 + left + right + up + down

        ans = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                ans = max(ans, Island(i, j)))
        return ans

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) ->int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0
                stack = [(i, j)]
                while stack:
                    ci, cj = stack.pop()
                    if ci < 0 or cj < 0 or ci == len(grid) or cj == len(grid[0]):
                        continue
                    cur += 1
                    grid[ci][cj] = 0
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        next_i, next_j = ci + di, cj + dj
                        stack.append((next_i, next_j))
                        stack.append((next_i, next_j))
                ans = max(ans, cur)

        return ans
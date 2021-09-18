import collections
from typing import List


class Solution:
    # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        def dfs(grid, r, c):
            if 0 <= r < n and 0 <= c < m and grid[r][c] == '1':
                # 设置为0，以后不再遍历
                grid[r][c] = '0'
                dfs(grid, r-1, c)
                dfs(grid, r+1, c)
                dfs(grid, r, c-1)
                dfs(grid, r, c+1)
                # 这种方法不行
                # for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                #     dfs(grid, r + i, r + j)

        for r in range(n):
            for c in range(m):
                # 当为1时，将1所属的岛屿全部遍历一遍
                # 遍历之后，将所有元素设置为0
                if grid[r][c] == '1':
                    print(r, c)
                    res += 1
                    dfs(grid, r, c)
        return res

    # BFS
    def numIslands_bfs(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if not n:
            return 0
        
        def bfs(grid, r, c):
            grid[r][c] = '0'
            que = collections.deque()
            que.append([r, c])
            while que:
                r, c = que.popleft()
                
        res = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    res += 1
                    bfs(grid, r, c)
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

ins = Solution()
print(ins.numIslands(grid))
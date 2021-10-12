import collections
from sys import path

from typing import List
class Solution:
    def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        def in_area(i, j):
            return 0 <= i < m and 0 <= j < n 
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)]

        m, n = len(grid), len(grid[0])
        
        que = collections.deque()
        que.append((0, 0))
        path_len = 0
        while que:
            sz = len(que)
            for i in range(sz):
                cur = que.popleft()
                r, c = cur
                # 不能是1
                if grid[r][c] == 1:
                    continue
                if r == m- 1 or c == n - 1:
                    # 到终点了
                    return path_len
    
                grid[r][c] = 1 # 标记
                for i, j in directions:
                    rr, cc = r + i, c + j
                    if in_area(i, j):
                        que.append((rr, cc))
        
        return -1
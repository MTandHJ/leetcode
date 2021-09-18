

from typing import List

class Solution:
    def largestIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        idx_island = 2
        mark_island = dict()

        # 判断是否在正方形里面
        def in_area(i, j):
            return 0 <= i < m and 0 <= j < n
        # 计算一个岛屿的面积，使用1来判断是否是岛屿
        # 第几个岛屿，开始的i，j是多少
        def area_size(idx_island, i, j):
            if not in_area(i, j):
                return 0
            
            if grid[i][j] != 1:
                return 0
            
            grid[i][j] = idx_island
            return 1 \
                + area_size(idx_island, i-1, j) \
                    + area_size(idx_island, i+1, j) \
                        + area_size(idx_island, i, j-1) \
                            + area_size(idx_island, i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = area_size(idx_island, i, j)
                    mark_island[idx_island] = size
                    idx_island += 1
                
        if len(mark_island) == 0:
            # 只填一个，所以最后得到的面积为1
            return 1
        # 不用填了，已经是最大的了
        if max(mark_island) == m*n:
            return m * n
        
        def area_idx(i, j):
            if in_area(i, j):
                idx = grid[i][j]
                if idx == 0:
                    return 0, 0 # 
                size = mark_island[idx]
                return idx, size
        
        def neighbor_areas(i, j):
            area_dict = dict()
            moves = {(-1, 0), (1, 0), (0, -1), (0, 1)}
            for ii, jj in moves:
                r = i + ii
                c = j + jj
                idx, size = area_idx(r, c)
                if idx not in area_dict:
                    area_dict.update({idx:size})
            return sum(area_dict.values())
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    size = 1 + neighbor_areas(i, j)
                    res = max(res, size)
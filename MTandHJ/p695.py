

from typing import List

from base import version


class Solution:

    @version("60ms, 17.9mb")
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        grid = [[0] + col + [0] for col in grid]
        grid.insert(0, [0] * (width + 2))
        grid.append([0] * (width + 2))

        def search(m, n):
            grid[m][n] = 0
            area = 1
            for l, r in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i, j = m + l, n + r
                if grid[i][j] == 1:
                    area += search(i, j)
            return area

        areas = [0]
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if grid[i][j] == 1:
                    areas.append(search(i, j))
        return max(areas)

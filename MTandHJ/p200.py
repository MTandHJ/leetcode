

from typing import List

from base import version


class Solution:

    @version("96ms, 25.2mb")
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        grid = [[0] + list(map(int, row)) + [0] for row in grid]
        grid.insert(0, [0] * (width + 2))
        grid.append([0] * (width + 2))

        nums = 0
        for m in range(1, height + 1):
            for n in range(1, width + 1):
                if grid[m][n] == 0:
                    continue
                nums += 1
                stack = [(m, n)]
                while stack:
                    i, j = stack.pop()
                    grid[i][j] = 0
                    for l, r in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                        if grid[i + l][j + r]:
                            stack.append((i + l, j + r))
        return nums



from typing import List

from base import version


class Solution:

    @version("84ms, 16mb")
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = heights
        atlantic = [[item for item in row] for row in heights]
        height, width = len(heights), len(heights[0])

        def dfs(m, n, heights, prev):
            if (0 <= m <= height - 1) and (0 <= n <= width - 1) and heights[m][n] != 'A' and heights[m][n] >= prev:
                prev = heights[m][n]
                heights[m][n] = 'A'
                dfs(m - 1, n, heights, prev)
                dfs(m, n - 1, heights, prev)
                dfs(m + 1, n, heights, prev)
                dfs(m, n + 1, heights, prev)

        for m in range(height):
            dfs(m, 0, pacific, -1)
            dfs(m, width - 1, atlantic, -1)
        for n in range(width):
            dfs(0, n, pacific, -1)
            dfs(height - 1, n, atlantic, -1)
        
        ans = []
        for m in range(height):
            for n in range(width):
                if pacific[m][n] == 'A' and atlantic[m][n] == 'A':
                    ans.append([m, n])
        return ans


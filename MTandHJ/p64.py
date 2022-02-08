

from typing import List

from base import version


class Solution:

    @version("88ms, 20.4mb")
    def minPathSum(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        memory = {(0, 0): grid[0][0]}
        def search(m, n):
            if memory.get((m, n), None) is None:
                ans = float('inf')
                for l, r in [(-1, 0), (0, -1)]:
                    i, j = m + l, n + r
                    if (0 <= i < height) and (0 <= j < width):
                        ans = min(ans, search(i, j) + grid[m][n])
                memory[(m, n)] = ans
            return memory[(m, n)]
        ans = search(height - 1, width - 1)
        return ans 

    @version("40ms, 15.3mb")
    def minPathSum(self, grid: List[List[int]]) -> int:
        prev = [float('inf')] * len(grid[0])
        cur = [0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur.append(min(cur[-1], prev[j]) + grid[i][j])
            prev, cur = cur[1:], [float('inf')]
        return prev[-1]


test = Solution()
test.minPathSum(
    [[1,2,5],[3,2,1]]
)

        
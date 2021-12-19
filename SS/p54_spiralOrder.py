

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        visited = [[False] * n for _ in range(m)]
        total = m * n
        order = [0] * total

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0
        for num in range(total):
            order[num] = matrix[i][j]
            visited[i][j] = True
            ni, nj = i + directions[idx][0], j + directions[idx][1]
            if not (0 <= ni < m and 0 <= nj < n and not visited[ni][nj]):
                idx = (idx + 1) % 4
            i += directions[idx][0]
            j += directions[idx][1]
        return order

matrix = [[1,2,3],[4,5,6],[7,8,9]]
ins = Solution()
print(ins.spiralOrder(matrix))
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(ins.spiralOrder(matrix))
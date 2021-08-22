

from typing import List
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]

        zeros_pos = [(i, j) for i in range(n) for j in range(n) if matrix[i][j] == 0]

        q = [zeros_pos]
        seen = set(zeros_pos)

        while q:
            i, j = q.pop(0)
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.append((ni, nj))
                
        return dist



from typing import List

class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        col0 = any(matrix[i][0] for i in range(m))
        row0 = any(matrix[0][j] for j in range(n))

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0

        if row0:
            for j in range(n):
                matrix[0][j] = 0
        
        if col0:
            for i in range(m):
                matrix[i][0] = 0
        

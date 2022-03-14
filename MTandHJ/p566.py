

from typing import List

from base import version

class Solution:

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c: return mat
        return [[mat[(i * c + j) // n][(i * c + j) % n] for j in range(c)] for i in range(r)]


from typing import List
class Solution:
    # 两步旋转法:
    # 首先:
    # 1. 先对称,再水平旋转
    # 2. 先水平旋转,再对称

    # 1. 先对称,再水平旋转
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 再列旋转
        for j in range(n // 2):
            for i in range(n):
                matrix[i][n-j-1], matrix[i][j] = matrix[i][j], matrix[i][n-j-1]


    # 先行旋转,
    # 再对称
    def rotate_2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 先行旋转
        # 再对称旋转
        for i in range(n // 2):
            for j in range(n):
                matrix[n-i-1][j], matrix[i][j] = matrix[i][j], matrix[n-i-1][j]
            
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i]  = matrix[j][i], matrix[i][j]

    # 直接只用一个公式
    def rotate_3(self, matrix:List[List[int]]) -> None:
        n = len(matrix)
        new_matrix = [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[i][n-j-1] = matrix[j][i]
                # new_matrix[n-i-1][j] = matrix[j][i]

        matrix[:] = new_matrix
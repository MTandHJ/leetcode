

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[int]]):
        maxSide = 0
        if not matrix or not matrix[0]:
            return maxSide
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    # 遇到一个1作为正方形的左上角
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形的边长
                    currentMaxSide = min(rows-i, cols-j)
                    for k in range(1, currentMaxSide):
                        flag = True
                        if matrix[i+k][j+k] == '0':
                            break
                        for m in range(k):
                            if matrix[i+k][j+m] == '0' \
                                or matrix[i+m][j+k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break
        return flag

    def maximalSquare2(self, matrix: List[List[int]]):
        maxSide = 0
        if not matrix or not matrix[0]:
            return maxSide
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                maxSide = max(maxSide, dp[i][j])
        return maxSide * maxSide


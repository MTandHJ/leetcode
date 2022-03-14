

from typing import List

from base import version


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = top = 0
        right, bottom = len(matrix) - 1, len(matrix[0]) - 1
        def search(u, v, s, t):
            if u > s or v > t:
                return False
            if u == s and v == t:
                return matrix[u][v] == target
            x = (u + s + 1) // 2
            y = (v + t + 1) // 2
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                return search(x, y, s, t) or search(u, y, x - 1, t) or search(x, v, s, y - 1)
            else:
                return search(u, v, x - 1, y - 1) or search(u, y, x - 1, t) or search(x, v, s, y - 1)
        return search(left, top, right, bottom)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, right = 0, n - 1
        while top < m and right >= 0:
            if matrix[top][right] == target:
                return True
            elif matrix[top][right] > target:
                right -= 1
            else:
                top += 1
        return False


test = Solution()
test.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
###### hard ######

from typing import List

class Solution:
    def maximalRectangle(self, matrix:List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0

        n = len(matrix[0])
        left = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j-1] + 1
        print(left)
        
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = left[i][j]
                print(width)
                area = width
                # for k in range(i-1, -1, -1):
                for k in range(i-1, 0, -1):
                    width = min(width, left[k][j])
                    area = max(area, (i-k+1)*width)
                # print(ret)
                ret = max(ret, area)

        return ret

class Solution:
    def maximalRectangle(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left = [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j-1] +1


        ret = 0
        for j in range(n):
            up = [i for i in range(m)]
            down = [j for j in range(n)]
            


if __name__ == '__main__':
    ins = Solution()
    # matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = [["1"]]
    print(ins.maximalRectangle(matrix))


#### medium ########
# In: matrix
# out: list

# record:
# June 20, 2021. 11:08

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        N, M = len(mat), len(mat[0])

        result, intermediate = [], []
        for d in range(N+M-1):
            intermediate.clear()
            
            if d < M:
                r = 0
                c = d
            else:
                r = d - M + 1
                c = M - 1
            
            while r < N and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result


class Solution:
    def findDiagonalOrder(self, mat:List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        N, M = len(mat), len(mat[0])
        result, intermediate = [], []

        for d in range(N+M-1):
            intermediate.clear()
            r, c = 0, 0
            if d < M:
                r = 0
                c = d
            else:
                r = d - M + 1
                c = M - 1
            
            while r < N and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        
        return result

if __name__ == "__main__":
    ins = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(ins.findDiagonalOrder(mat))






class Solution:
    def pathAvaliable(self, matrix, starts, ends):
        
        def inMatrix(i, j, start, end):
            # n = len(matrix)
            # m = len(matrix[0])
            return start[0] <= i <= end[0] and start[1] <= j <= end[1]

        def sub(matrix, start, end):
            # directio]
            j = start[1]
            for i in range(start[0], end[0]+1):
                # while start[1] <= j <= end[1]:
                if inMatrix(i+1, j, start, end) and inMatrix(i, j+1, start, end):
                    if matrix





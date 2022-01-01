

from typing import List

from base import version


class Solution:

    @version("80ms, 15.3mb")
    def solveSudoku(self, board: List[List[str]]) -> None:
        cond_row = []
        cond_col = [set() for _ in range(9)]
        cond_block = [[set() for _ in range(3)] for _ in range(3)]
        for i, row in enumerate(board):
            cond_row.append(set(row))
            for j, item in enumerate(row):
                cond_col[j].add(item)
                cond_block[i // 3][j // 3].add(item)
        pools = set('123456789')
        
        def add(i, j, num):
            cond_row[i].add(num)
            cond_col[j].add(num)
            cond_block[i // 3][j // 3].add(num)
            board[i][j] = num
        
        def remove(i, j, num):
            cond_row[i].remove(num)
            cond_col[j].remove(num)
            cond_block[i // 3][j // 3].remove(num)
            board[i][j] = '.'

        def search(order):
            if order == 81:
                return True
            m, n = order // 9, order % 9
            if board[m][n] != '.':
                return search(order + 1)
            else:
                for num in pools - cond_row[m] - cond_col[n] - cond_block[m // 3][n // 3]:
                    add(m, n, num)
                    if search(order + 1):
                        return True
                    remove(m, n, num)
                return False
        search(0)


# test = Solution()
# test.solveSudoku(

# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# )


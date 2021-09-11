

from typing import List


class Solution:
    def solveNQueens(n: int) -> List[int]:
        self.res = []
        board = [['.'] * n for _ in range(n)]

        self.backtrack(board, 0)
        return self.res
    
    def backtrack(self, board: List[List[str]], row: int) -> List[List[str]]:
        if row == len(board):
            self.res.append(board)
            return 
        
        n = len(board[row])
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
                
            # 做选择
            board[row][col] = 'Q'
            # make next decision
            self.backtrack(board, row + 1)
            # back decision
            board[row][col] = '.'

    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        n = len(board)
        # 检查列中是否有n皇后的冲突
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        
        for i in range(row-1, j)
        
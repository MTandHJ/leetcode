from typing import List
import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [['.'] * n for _ in range(n)]
        self.backtrack(board, 0)
        # self.res = [''.join(item) for item in self.res]
        ans = []
        for item in self.res:
            ans.append([''.join(li) for li in item])
        return ans
    
    def backtrack(self, board, row: int):
        # print(board)
        if row == len(board):
            self.res.append(copy.deepcopy(board))
            return 
        
        n = len(board[0])
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'
    
    def isValid(self, board: List[str], row: int, col: int):
        n = len(board)
        # 检查列是否有冲突，
        # 要求这一行有了Q，这一行的其他列就不能有Q
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        # 检查右上方是否有冲突
        i, j = row - 1, col + 1
        while i > -1 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        # 检查左上方是否有冲突
        i, j = row - 1, col - 1
        while i > -1 and j > -1:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        return True

ins = Solution()
print(ins.solveNQueens(4))
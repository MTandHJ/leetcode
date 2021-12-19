

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return 
            
            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j//3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i//3][j//3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i//3][j//3][digit] = False
                if valid:
                    return 
        
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _i in range(3)] for _b in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = True
                    column[j][digit] = True
                    block[i//3][j//3][digit] = True
        dfs(0)

    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(pos: int):
            nonlocal valid
            # print(pos)
            
            if pos == len(spaces):
                print(pos)
                valid = True
                return 
            i, j = spaces[pos]
            for digit in range(9):
                print(pos, i, j)
                if line[i][digit] == column[j][digit] == block[i//3][j//3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i//3][j//3][digit] =True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i//3][j//3][digit] = False
                # print(valid)
                if valid:
                    print(pos)
                    return 
        
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _b in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = True
                    column[j][digit] = True
                    block[i//3][j//3][digit] = True
        # print(len(spaces))
        dfs(0)

ins = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ins.solveSudoku2(board)
print(board)
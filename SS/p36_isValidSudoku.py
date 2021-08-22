
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[int]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]

        block = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    block[box_index][num] = block[box_index].get(num, 0) + 1

                    if row[i][num] > 1 or col[j][num] > 1 or block[box_index][num] > 1:
                        return False
                    
            return True



from typing import List

from base import version


class Solution:

    @version("40ms, 18.3mb")
    def solve(self, board: List[List[str]]) -> None:
        height, width = len(board), len(board[0])
        proxy = [[item for item in row] for row in board]
        for m in range(height):
            for n in range(width):
                board[m][n] = 'X'
        
        def search(m, n):
            if proxy[m][n] == 'X':
                return 0
            stack = [(m, n)]
            while stack:
                m, n = stack.pop()
                board[m][n] = 'O'
                proxy[m][n] = 'X'
                for l, r in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    i, j = m + l, n + r
                    if (0 <= i <= height - 1) and (0 <= j <= width - 1) and proxy[i][j] == 'O':
                        stack.append((i, j))

        for m in (0, height - 1):
            for n in range(width):
                search(m, n)
        for n in (0, width - 1):
            for m in range(height):
                search(m, n)


                



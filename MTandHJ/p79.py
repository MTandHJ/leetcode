


from typing import List

from base import version


class Solution:

    @version("4652ms, 15.2mb")
    def exist(self, board: List[List[str]], word: str) -> bool:
        height, width = len(board), len(board[0])

        def search(x, y, road, word):
            if len(word) == 0:
                return True
            road = road | {(x, y)}
            for l, r in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                i, j = x + l, y + r
                if (0 <= i < height) and (0 <= j < width) and (i, j) not in road:
                    if board[i][j] == word[0] and search(i, j, road, word[1:]):
                        return True
            return False

        for m in range(height):
            for n in range(width):
                if board[m][n] == word[0] and search(m, n, set(), word[1:]):
                    return True
        return False
                


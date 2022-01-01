

from typing import List

from base import version


class Solution:

    @version("72ms, 15.3mb")
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = set()
        def check(i, j):
            for m, n in queens:
                if m == i or n == j or abs(m - i) == abs(n - j):
                    return False
            return True
        def search(i):
            if i == n:
                return [[]]
            ans = []
            for j in range(n):
                if check(i, j):
                    queens.add((i, j))
                    nxt = search(i + 1)
                    if nxt:
                        for item in nxt:
                            each = ['.'] * n
                            each[j] = 'Q'
                            ans.append([''.join(each)] + item)
                    queens.remove((i, j))
            return ans
        return search(0)
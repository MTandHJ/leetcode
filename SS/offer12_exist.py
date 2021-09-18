from typing import List
class Solution:
    def exist(self, board:List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def check(i:int, j:int, k:int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            res = False

            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            res = True
                            break
            
            visited.remove((i, j))
            return res

        h, w = len(board), len(board[0])
        visited = set()

        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(i:int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) -1:
                return True
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            visited.add((i, j))
            res = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if check(newi, newj, k+1):
                        res = True
                        break
            
            visited.remove((i, j))
            return res
        
        visited = set()
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if check(i, j, 0):
                    return True
        
        return False

if __name__ == '__main__':
    ins = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(ins.exist(board, word))
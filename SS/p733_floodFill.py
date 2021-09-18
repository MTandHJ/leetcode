
from typing import Collection, List

class Solution:
    def floddFill(self, image:List[List[int]], sr:int, sc:int, newColor:int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(r:int, c:int) -> None:
            if image[r][c] == color:
                image[r][c] = newColor
                # 左，右，上，下
                if r >= 1: dfs(r-1, c)
                if r+1 < n: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < m: dfs(r, c+1)
        
        dfs(sr, sc)
        return image

class Solution:
    def floddFill(self, image:List[List[int]], sr:int, sc:int, newColor:int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        que = []
        que.append((sr, sc))
        color = image[sr][sc]

        while not que:
            point = que.pop(0)
            r, c = point
            image[r][c] = newColor
            for i, j in directions:
                new_i = r + i
                new_j = c + j
                if 0 <= new_i < len(image) \
                    and 0 <= new_j < len(image[0]) \
                        and image[new_i][new_j] == color:
                        que.append((new_i, new_j))
        
        return image
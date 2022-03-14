

from typing import List

from base import version

class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        UNCORLORED, BLACK, WHITE = -1, 0, 1
        colors = [UNCORLORED] * len(graph)
        for root in range(len(graph)):
            if colors[root] != UNCORLORED:
                continue
            colors[root] = BLACK
            q = [root]
            while q:
                root = q.pop()
                col = BLACK if colors[root] == WHITE else WHITE
                for nxt in graph[root]:
                    if colors[nxt] == UNCORLORED:
                        q.append(nxt)
                        colors[nxt] = col
                    elif colors[nxt] != col:
                        return False
        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        UNCORLORED, BLACK, WHITE = -1, 0, 1
        colors = [UNCORLORED] * len(graph)
        def dfs(root, color=BLACK):
            colors[root] = color
            col = BLACK if color == WHITE else WHITE
            for nxt in graph[root]:
                if colors[nxt] == UNCORLORED:
                    dfs(nxt, col)
                elif colors[nxt] == color:
                    assert False
        try:
            for root in range(len(graph)):
                if colors[root] == UNCORLORED:
                    dfs(root)
            return True
        except AssertionError:
            return False
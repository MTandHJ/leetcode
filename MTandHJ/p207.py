

from typing import List

import collections

from base import version

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {k:[] for k in range(numCourses)}
        for border in prerequisites:
            graph[border[0]].append(border[1])
        INACTIVE, ACTIVE, OVER = -1, 1, 0
        state = [INACTIVE] * numCourses
        def dfs(root):
            state[root] = ACTIVE
            while graph[root]:
                nxt = graph[root].pop()
                if state[nxt] == INACTIVE:
                    dfs(nxt)
                elif state[nxt] == ACTIVE:
                    assert False
            state[root] = OVER
        try:
            for root in graph.keys():
                if state[root] == INACTIVE:
                    dfs(root)
            return True
        except AssertionError:
            return False


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevs = {k:set() for k in range(numCourses)}
        after = {k:set() for k in range(numCourses)}
        for pair in prerequisites:
            prevs[pair[0]].add(pair[1])
            after[pair[1]].add(pair[0])
        q = []
        for root, val in prevs.items():
            if not val:
                q.append(root)
        while q:
            root = q.pop()
            for nxt in after[root]:
                prevs[nxt].remove(root)
                if not prevs[nxt]:
                    q.append(nxt)
        for root, val in prevs.items(): 
            if val:
                return False
        return True

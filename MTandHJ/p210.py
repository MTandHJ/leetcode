

from typing import List


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {k:[] for k in range(numCourses)}
        INACTIVE, ACTIVE, OVER = -1, 1, 0
        state = [INACTIVE] * numCourses
        order = []
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        def dfs(root):
            state[root] = ACTIVE
            while graph[root]:
                nxt = graph[root].pop()
                if state[nxt] == INACTIVE:
                    dfs(nxt)
                elif state[nxt] == ACTIVE:
                    assert False
            state[root] = OVER
            order.append(root)
        try:
            for root in range(numCourses):
                if state[root] == INACTIVE:
                    dfs(root)
            return order
        except AssertionError:
            return []


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prevs = [0] * numCourses
        after = {k:[] for k in range(numCourses)}
        for pair in prerequisites:
            prevs[pair[0]] += 1
            after[pair[1]].append(pair[0])
        q = []
        for k, val in enumerate(prevs):
            if not val:
                q.append(k)
        order = []
        while q:
            root = q.pop()
            order.append(root)
            for nxt in after[root]:
                prevs[nxt] -= 1
                if not prevs[nxt]:
                    q.append(nxt)
        if sum(prevs):
            return []
        else:
            return order
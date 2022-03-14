

from typing import List

from base import version

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connected = []
        for x, y in edges:
            left = right = None
            for i, part in enumerate(connected):
                if x in part:
                    left = i
                if y in part:
                    right = i
            if left is None and right is None:
                newpart = {x, y}
            elif left is None:
                newpart = {x} | connected[right]
            elif right is None:
                newpart = {y} | connected[left]
            elif left == right:
                return [x, y]
            else:
                newpart = connected[left] | connected[right]
            newconnected = [newpart]
            for i, part in enumerate(connected):
                if i not in (left, right):
                    newconnected.append(part)
            connected = newconnected


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [k for k in range(n + 1)]
        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        def union(index1, index2):
            parent[find(index1)] = find(index2)
        for x, y in edges:
            if find(x) != find(y):
                union(x, y)
            else:
                return (x, y)
            


from typing import Counter, List

from typing import List


class UnionFind():
    def __init__(self, count, parent) -> None:
        self.count = count 
        self.parent = parent

    def getCount(self):
        return self.count
    
    def addCount(self):
        self.count += 1
    
    def UnionFind(self, n):
        
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]):
        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        unionFind = UnionFind(m * n)



from typing import List

from base import version


class Solution:
    @version("300ms, 39.8mb")
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        length = len(points)
        mark = points[0][1]
        count = 1
        for i in range(1, length):
            if points[i][0] > mark:
                count += 1
                mark = points[i][1]
            else:
                mark = min(mark, points[i][1])
            
        return count

    @version("similar to p435: 272ms, 39.9mb")
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))
        length = len(points)
        mark = points[0][1]
        count = 1
        for i in range(1, length):
            if points[i][0] > mark:
                count += 1
                mark = points[i][1]
        return count


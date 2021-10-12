

from typing import List


class Solution:
    def findMinArrowShots(self, intervals: List[int]) -> int:
        n = len(intervals)
        if n < 2:
            return n
        
        intervals.sort(key=lambda x: x[1])
        right = intervals[0][1]
        
        res = 0
        for i in range(1, n):
            if intervals[i][0] > right:
                res += 1
                right = intervals[i][1]
        return res
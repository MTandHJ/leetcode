

from typing import List

from base import version


class Solution:

    @version("364ms, 38.8mb")
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        length = len(intervals)
        mark = intervals[0][1]
        count = 1
        for i in range(1, length):
            if intervals[i][0] >= mark:
                count += 1
                mark = intervals[i][1]
        return length - count

                









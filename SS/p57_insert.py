
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[int]:
        left = newInterval[0]
        right = newInterval[1]

        placed = False
        res = []
        for interval in intervals:
            # 在右边，没有交集
            if interval[0] > right:
                if not placed:
                    res.append([left, right])
                    placed = True
                res.append(interval)
            # 在左边，没有交集
            elif interval[0] < left:
                res.append(interval)
            else:
                # 有交集
                left = min(left, interval[0])
                right = max(right, interval[1])
        if not placed:
            res.append(newInterval)
        return res
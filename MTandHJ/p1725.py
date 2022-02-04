

from typing import List

from base import version




class Solution:

    @version("52ms, 15.3mb")
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = max(map(min, rectangles))
        count = 0
        for rectangle in rectangles:
            if min(rectangle) >= maxLen:
                count += 1
        return count

    @version("44ms, 15.3mb")
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        maxLen = -1
        for l, w in rectangles:
            cur = min(l, w)
            if cur == maxLen:
                count += 1
            elif cur > maxLen:
                maxLen = cur
                count = 1
        return count


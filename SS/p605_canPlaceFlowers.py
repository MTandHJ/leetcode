

from typing import List


class Solution:
    def canPlaceFlowers(self, flowrbed: List[int], n: int) -> bool:
        res = 0
        m = len(flowrbed)
        prev = -1 
        for i in range(m):
            if flowrbed[i] == 1:
                if prev < 0:
                    res += i / 2
                else:
                    res += (i - prev - 2) // 2
                prev = i 
        if prev < 0:
            res += (m + 1) // 2
        else:
            res += (m - prev - 1) // 2
        return res >= n
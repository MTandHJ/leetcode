
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res= 0, len(height) - 1, 0
        while i < j:
            # res = max(min(height[i], height[j]) * (j - i), res)
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
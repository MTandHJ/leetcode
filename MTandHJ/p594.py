


from typing import List

import collections

class Solution:

    def findLHS(self, nums: List[int]) -> int:
        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        theMax = 0
        for key, val in counts.items():
            if key - 1 in counts:
                theMax = max(theMax, val + counts[key - 1])
        return theMax



from typing import List
from collections import defaultdict

from base import version


class Solution:

    @version("32ms, 15.2mb")
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        factors = defaultdict(int)
        for num in nums:
            factors[num] += 1
        pools = sorted(list(set(nums)))
        def search(cur):
            ans = [[]]
            for i, num in enumerate(pools[cur:], cur):
                if factors[num]:
                    factors[num] -= 1
                    for item in search(i):
                        ans.append([num] + item)
                    factors[num] += 1
            return ans
        return search(0)

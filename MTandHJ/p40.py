

from typing import List
from collections import defaultdict

from base import version


class Solution:

    @version("over time limits")
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def search(candidates, target):
            if target == 0:
                return [tuple()]
            elif target < 0:
                return []
            ans = []
            for i, candidate in enumerate(candidates):
                for item in search(candidates[i + 1:], target - candidate):
                    ans.append((candidate,) + item)
            return ans
        return list(set(search(candidates, target)))

    @version("68ms, 15.1mb")
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        factors = defaultdict(int)
        for candidate in candidates:
            factors[candidate] += 1
        pools = sorted(list(set(candidates)))
        def search(target, cur):
            if target == 0:
                return [[]]
            elif target < 0:
                return []
            ans = []
            for i, candidate in enumerate(cur, pools[cur:], cur):
                if factors[candidate]:
                    factors[candidate] -= 1
                    for item in search(target - candidate, i):
                        ans.append([candidate] + item)
                    factors[candidate] += 1
            return ans 
        return search(target, 0)
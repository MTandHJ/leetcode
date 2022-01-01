

from typing import List

from base import version


class Solution:

    @version("64ms, 15mb")
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def search(candidates, target):
            if target == 0:
                return [[]]
            elif target < 0:
                return []
            ans = []
            for i, candidate in enumerate(candidates):
                for item in search(candidates[i:], target - candidate):
                    ans.append([candidate] + item)
            return ans
        return search(candidates, target)


from typing import List

from base import version


class Solution:

    @version("32ms, 15.1mb")
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        def search(cur, n, k):
            if k == 0 and n == 0:
                return [[]]
            elif k == 0 and n != 0:
                return []
            elif k != 0 and n == 0:
                return []
            ans = []
            for i, num in enumerate(nums[cur:], cur):
                for item in search(i + 1, n - num, k - 1):
                    ans.append([num] + item)
            return ans
        return search(0, n, k)


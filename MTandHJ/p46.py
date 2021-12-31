

from typing import List

from base import version


class Solution:

    @version("28ms, 15.1mb")
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        pool = set()
        def dfs(level):
            if level == len(nums) - 1:
                return [list(nums - pool)]
            ans = []
            for num in nums - pool:
                pool.add(num)
                for item in dfs(level + 1):
                    ans.append([num] + item)
                pool.remove(num)
            return ans
        return dfs(0)

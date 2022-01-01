

from typing import List

from base import version


class Solution:

    @version("36ms, 15.1mb")
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        prev = [[]]
        prev_mark = [0]
        while prev:
            cur = []
            cur_mark = []
            for i, item in enumerate(prev):
                for j, num in enumerate(nums[prev_mark[i]:], prev_mark[i] + 1):
                    cur.append(item + [num])
                    cur_mark.append(j)
            ans += cur
            prev = cur
            prev_mark = cur_mark
        return ans
                
    @version("44ms, 15.2mb")
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def search(cur):
            ans = [[]]
            for i, num in enumerate(nums[cur:], cur + 1):
                for item in search(i):
                    ans.append([num] + item)
            return ans
        return search(0)

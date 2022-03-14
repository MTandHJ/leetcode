

from typing import List

from base import version

class Solution:

    @version("64ms, 16.6mb")
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1 for _ in range(len(nums))]
        for _ in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    ans[stack[-1]] = nums[i]
                    stack.pop()
                if ans[i] == -1:
                    stack.append(i)
        return ans
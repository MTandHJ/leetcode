

from typing import List

from base import version

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = list(set(nums))
        nums.sort()
        left = nums[0]
        memory = {left}
        length = 0
        for right in nums[1:]:
            if len(memory) != (right - left):
                length = max(length, len(memory))
                left = right
                memory = {left}
            else:
                memory.add(right)
        length = max(length, len(memory))
        return length


    @version("over time limits")
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        start, end = min(nums), max(nums)
        x = y = 0
        for n in range(start, end + 1):
            if n in nums:
                x = x + 1
            else:
                y = max(x, y)
                x = 0
        y = max(x, y)
        return y




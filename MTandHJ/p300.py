


from typing import List

from base import version


class Solution:

    @version("3056ms, 15.4mb")
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = {-1:1}
        for i, num in enumerate(nums):
            tmp = 1
            for j in range(i-1, -1, -1):
                if num > nums[j]:
                    tmp = max(memory[j] + 1, tmp)
            memory[i] = tmp
        return max(memory.values())

    def lengthOfLIS(self, nums: List[int]) -> int:

test = Solution()
test.lengthOfLIS([1,3,6,7,9,4,10,5,6])


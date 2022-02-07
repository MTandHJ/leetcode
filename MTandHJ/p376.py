

from typing import List

from base import version


class Solution:
    
    @version("dp: 176ms, 15mb")
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dpp = [1] * len(nums)
        dpm = [1] * len(nums)
        for j in range(len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dpp[j] = max(dpp[j], dpm[i] + 1)
                elif nums[j] < nums[i]:
                    dpm[j] = max(dpm[j], dpp[i] + 1)
        return max(dpp + dpm)

    @version("44ms, 14.9mb")
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cur = 999
        count = 1
        for x, y in zip(nums[:-1], nums[1:]):
            if x < y:
                up = 1
            elif x > y:
                up = 2
            else:
                continue
            if up != cur:
                count += 1
            cur = up
        return count
    
test = Solution()
test.wiggleMaxLength([1, 7, 4, 9, 2, 5])
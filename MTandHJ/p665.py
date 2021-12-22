

from typing import List

from base import version


class Solution:

    @version("40ms, 15.8mb")
    def checkPossibility(self, nums: List[int]) -> bool:
        tom, jerry = -float('inf'), -float('inf')
        flag = iter((1,))
        try:
            for num in nums:
                if num < jerry:
                    next(flag)
                    if tom <= num:
                        tom, jerry = num, num
                    else:
                        tom, jerry = jerry, jerry
                else:
                    tom, jerry = jerry, num
            return True
        except StopIteration:
            return False

    
    @version("false yet nice try.")
    def checkPossibility(self, nums: List[int]) -> bool:
        nums = [nums[0]] + nums + [nums[-1]]
        nums = [(min(l, r), max(l, r)) for l, r in zip(nums[:-1], nums[1:])]
        nums.sort(key=lambda x: (x[1], x[0]))
        mark = nums[0][1]
        flag = iter((1,))
        try:
            for num in nums[1:]:
                if num[0] < mark:
                    print(num)
                    next(flag)
                else:
                    mark = num[1]
            return True
        except StopIteration:
            return False

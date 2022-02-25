

from typing import List

from base import version


class Solution:

    @version("56ms, 15.7mb")
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        allSum = sum(nums)
        curSum = 0
        theMin = float('inf')
        for k, num in enumerate(nums, 1):
            curSum += num
            length1, length2 = k, len(nums) - k
            u = num if length1 > length2 else nums[k]
            value = allSum - curSum * 2 + (length1 - length2) * u
            theMin = value if value < theMin else theMin
        return theMin

    @version("quickSort: 40ms, 15.9mb")
    def minMoves2(self, nums: List[int]) -> int:
        def quickSort(nums):
            if len(nums) <= 1:
                return nums
            anchor = nums[0]
            left, right = [], []
            for num in nums[1:]:
                if num < anchor:
                    left.append(num)
                else:
                    right.append(num)
            return quickSort(left) + [anchor] + quickSort(right)
        nums = quickSort(nums)
        half = len(nums) // 2
        return sum(nums[-half:]) - sum(nums[:half])
        

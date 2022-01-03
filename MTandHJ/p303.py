

from typing import List

from base import version


class Solution:


    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cum_summation = [0]
        for num in self.nums:
            self.cum_summation.append(
                self.cum_summation[-1] + num
            )

    @version("76ms, 18.2mb")
    def sumRange(self, left: int, right: int) -> int:
        return self.cum_summation[right + 1] - self.cum_summation[left]




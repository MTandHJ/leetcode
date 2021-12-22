


from typing import List

from base import version


class Solution:

    @version("96ms, 25.3mb")
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        ans = -float('inf')
        prev = 0
        for num in nums:
            cur += num
            if cur - prev > ans:
                ans = cur - prev
            if cur < prev:
                prev = cur
        return ans

    @version("false try: it is similar to p121 ...")
    def maxSubArray(self, nums: List[int]) -> int:
        bottom, top = 0, nums[0]
        price = 0
        profits = [nums[0]]
        for num in nums:
            price += num
            if price < bottom:
                profits.append(top - bottom)
                top, bottom = price, price
            elif price > top:
                top = price
        profits.append(top - bottom)


from typing import List

import collections

from base import version


class Solution:

    @version("40ms, 16.5mb")
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = reduce(lambda x, y: x ^ y, nums)
        nums = set(nums)
        for num in nums:
            if (x ^ num) in nums:
                return [x, x ^ num]

    @version("40ms, 16.4mb")
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = collections.defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if cnt[num] == 2:
                del cnt[num]
        return list(cnt.keys())
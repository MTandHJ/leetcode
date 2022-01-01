

from typing import List

from base import version


class Solution:

    @version("76ms, 17.1mb")
    def combine(self, n: int, k: int) -> List[List[int]]:
        def search(nums, k):
            if k == 0:
                return [[]]
            ans = []
            for i, num in enumerate(nums[k-1:]):
                for item in search(nums[:i + k - 1], k - 1):
                    ans.append([num] + item)
            return ans
        nums = list(range(1, n + 1))[::-1]
        return search(nums, k)

test = Solution()
print(test.combine(4, 2))
            

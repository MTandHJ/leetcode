


from typing import List
from collections import defaultdict

from base import version


class Solution:

    @version("552ms, 21mb")
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        factors = set()
        pools = set(range(len(nums)))
        def search():
            ans = []
            for num in pools - factors:
                factors.add(num)
                for item in search():
                    ans.append([num] + item)
                factors.remove(num)
            if ans:
                return ans
            else:
                return [[]]
        results = set()
        for item in search():
            results.add(tuple(
                [nums[index] for index in item]
            ))
        return list(results)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        factors = defaultdict(int)
        for num in nums:
            factors[num] += 1
        pools = set(nums)
        def search():
            ans = []
            for num in pools:
                if factors[num] > 0:
                    factors[num] -= 1
                    for item in search():
                        ans.append([num] + item)
                    factors[num] += 1
            if ans:
                return ans
            else:
                return [[]]
        return search()


test = Solution()
test.permuteUnique([1,1,2])
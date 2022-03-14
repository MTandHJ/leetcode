

from base import *


class Solution:
    """
    >>> tester = Solution()
    >>> nums = [2, 7, 11, 9]
    >>> target = 9
    >>> tester.twoSum(nums, target)
    (0, 1)
    >>> nums = [6, 2, 4]
    >>> target = 6
    >>> tester.twoSum(nums, target)
    (1, 2)
    """
    @version("trivial: 36ms, 14.9mb")
    def twoSum(self, nums: List[int], target: int) -> Union(Tuple[int], int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        return -1

    @version("hash: 36ms, 15mb")
    def twoSum(self, nums: List[int], target: int) -> Union(Tuple[int], int):
        store = dict(zip(nums, range(len(nums))))
        for i, val in enumerate(nums):
            try:
                idx = store[target - val]
                if i != idx:
                    return i, idx
            except KeyError:
                pass
        return -1

    @version("hash: 40ms, 14.9mb")
    def twoSum(self, nums: List[int], target: int) -> Union(Tuple[int], int):
        store = dict()
        for i, val in enumerate(nums):
            try:
                idx = store[target - val]
                return i, idx
            except KeyError:
                store[val] = i
        return -1



if __name__ == "__main__":
    import doctest
    doctest.testmod()
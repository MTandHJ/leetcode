


from typing import List
from base import version

class Solution:

    @version("Time exceeds")
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length):
            for j in range(length):
                if i == j: continue
                if numbers[i] + numbers[j] == target:
                    return i + 1, j + 1
    
    @version("Simple")
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ < target:
                left += 1
            elif sum_ > target:
                right -= 1
            else:
                return left + 1, right + 1










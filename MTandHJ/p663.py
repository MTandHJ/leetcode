


from typing import List
from base import version


class Solution:

    @version("Time exceeds")
    def judgeSquareSum(self, c: int) -> bool:
        numbers = list(map(lambda x: x * x, range(c + 1)))
        left, right = 0, c
        while left <= right:
            sum_ = numbers[left] + numbers[right]
            if sum_ < c:
                left += 1
            elif sum_ > c:
                right -= 1
            else:
                return True
        return False

    @version("preprocess?")
    def judgeSquareSum(self, c: int) -> bool:
        import math
        end = int(math.sqrt(c)) + 1
        numbers = list(map(lambda x: x * x, range(end)))
        left, right = 0, len(numbers) - 1
        while left <= right:
            sum_ = numbers[left] + numbers[right]
            if sum_ < c:
                left += 1
            elif sum_ > c:
                right -= 1
            else:
                return True
        return False









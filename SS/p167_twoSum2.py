from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target:int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            cur = numbers[i] + numbers[j]
            if cur < target:
                i += 1
            elif cur > target:
                j -= 1
            else:
                return i+1, j+1
        return -1, -1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low, high = i+1, n -1
            while low <= high:
                mid = low + (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return i+1, mid+1
                elif numbers[mid] > target - numbers[i]:
                    high -= 1
                else:
                    low += 1
        return -1, -1
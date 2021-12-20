



from typing import List
from base import version
from sorts import MinHeap

class Solution:

    @version("sorted: 32ms")
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    @staticmethod
    def _sorted(nums: List) -> List:
        left, right = 0, len(nums)
        mark = nums[0]
        while left < right:
            right -= 1
            if nums[right] < mark:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
            while mark < nums[left]:
                left += 1

    @version("sorted: 356ms")
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = [-10 ** 5] * k
        for num in nums:
            if num > stack[0]:
                stack[0] = num
                stack.sort()
        return stack[0]

    def quicksort_(self, nums:List, low: int, high: int, k) -> List:
        if low < high and low <= len(nums) - k and high >= len(nums) - k:
            pivot = nums[low]
            left, right = low, high
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
                while left < right and pivot > nums[left]:
                    left += 1
                nums[left], nums[right] = nums[right], nums[left]

            self.quicksort_(nums, low=low, high=left-1, k=k) 
            self.quicksort_(nums, low=right+1, high=high, k=k)

    @version("844ms?")
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quicksort_(nums)
        return nums[-k]

    @version("minimum heap: 404ms")
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap()
        for num in nums:
            heap.add(num)
            if len(heap) > k:
                heap.pop()
        return heap.pop()
        

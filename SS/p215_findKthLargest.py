

from typing import List
import random

class Solution:
    def findKthLargest(self, nums, k: int) -> List[int]:
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, a: List, l: int, r: int, index: int):
        q = self.randomPartition(a, l, r)

        if q == index:
            return a[q]
        else:
            return self.quickSelect(a, q+1, r, index) if q < index else self.quickSelect(a, l, q-1, index)

    def randomPartition(a: List, l:int, r:int):
        i = random.randint(l, r)
        a[i], a[r] = a[r], a[i]
        return self.partition(a, l, r)
    
    def partition(self, a:List, l:int, r:int):
        x = a[r]
        i = l - 1
        for j in range(l, r):
            if a[j] <= x:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i+1], a[r] = a[r], a[i+1]
        return i+1

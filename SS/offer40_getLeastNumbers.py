

from typing import List
class Solution:
    def getLeastNumbers(self, arr: List[int]) -> List[int]:
        n = len(arr)
        l, r = 0, n-1
        i, j = l, r
        while i < j:
            while i < j and arr[j] >= arr[l]:
                j -= 1
            while i < j and arr[i] < arr[l]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
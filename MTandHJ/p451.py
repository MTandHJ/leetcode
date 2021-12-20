


from typing import List, Optional, Iterable, Dict
from collections import defaultdict

from base import version

def quicksort_(keys: List, bins: Dict, low: int, high: int) -> List:
    if low < high:
        pivot = bins[keys[low]]
        left, right = low, high
        while left < right:
            while left < right and bins[keys[right]] >= pivot:
                right -= 1
            keys[left], keys[right] = keys[right], keys[left]
            while left < right and pivot > bins[keys[left]]:
                left += 1
            keys[left], keys[right] = keys[right], keys[left]

        quicksort_(keys, bins, low=low, high=left-1) 
        quicksort_(keys, bins, low=right+1, high=high)

class Solution:

    @version("40ms")
    def frequencySort(self, s: str) -> str:
        bins = defaultdict(int)
        for ele in s:
            bins[ele] += 1
        keys = list(bins.keys())
        keys.sort(key=lambda x: bins[x], reverse=True)
        s = ''
        for key in keys:
            s += key * bins[key]
        return s

    @version("quick: 44ms")
    def frequencySort(self, s: str) -> str:
        bins = defaultdict(int)
        for ele in s:
            bins[ele] += 1
        keys = list(bins.keys())
        keys.sort(key=lambda x: bins[x], reverse=True)
        quicksort_(keys, bins, 0, len(keys) - 1)
        s = ''
        for key in keys[::-1]:
            s += key * bins[key]
        return s


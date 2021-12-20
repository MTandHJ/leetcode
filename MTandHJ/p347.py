


from typing import List, Optional, Iterable, Dict
from collections import defaultdict

from base import version
from sorts import MinHeap


class MinHeapForBin(MinHeap):

    def __init__(self, bins: Dict, data: Optional[Iterable] = None) -> None:
        self.bins = bins
        super().__init__(data=data)

    def get(self, index: int):
        return self.bins[self.data[index]]


class Solution:

    @version("44ms")
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bins = defaultdict(int)
        for num in nums:
            bins[num] += 1
        keys = list(bins.keys())
        keys.sort(key=lambda x: bins[x])
        return keys[-k:]

    @version("minimum heap: 116ms")
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bins = defaultdict(int)
        for num in nums:
            bins[num] += 1
        keys = list(bins.keys())
        heap = MinHeapForBin(bins, keys)
        while len(heap) > k:
            heap.pop()
        return heap.data
   
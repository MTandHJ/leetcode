

from typing import List

from base import version


class Solution:

    @version("36ms, 15.1mb")
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [flowerbed[0]] + flowerbed + [flowerbed[-1]]
        count = 0
        for i in range(1, len(flowerbed) - 1):
            if not (flowerbed[i] or flowerbed[i - 1] or flowerbed[i + 1]):
                count += 1
                flowerbed[i] = 1
        return count >= n

    @version("40ms, 15.2mb")
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left, right = -2, -1
        count = 0
        for right, flower in enumerate(flowerbed):
            if flower == 1:
                count += (right - left - 2) // 2
                left = right
        count += (right - left) // 2
        return count >= n
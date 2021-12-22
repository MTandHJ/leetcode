

from typing import List

from base import version


class Solution:

    @version("56ms, 16.2mb")
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        g = (child for child in g)
        s = sorted(s)
        s = (food for food in s)
        child = next(g)
        count = 0
        try:
            while True:
                food = next(s)
                if child <= food:
                    count += 1
                    child = next(g)
        except StopIteration:
            return count
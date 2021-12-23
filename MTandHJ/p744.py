



from typing import List

from base import version


class Solution:

    @version("28ms, 16.4mb")
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        while l < r:
            m = l + (r - l) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        return letters[l % len(letters)]

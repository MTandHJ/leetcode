

import collections

from base import version


class Solution:

    @version("80ms, 16.2mb")
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        count = collections.defaultdict(int)
        for item in s:
            count[item] += 1
        for item in t:
            count[item] -= 1
        for val in count.values():
            if val != 0:
                return False
        return True
        

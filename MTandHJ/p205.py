

from base import version


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counts = dict()
        for x, y in zip(s, t):
            if x in counts:
                x = counts[x]
                if x != y:
                    return False
            else:
                counts[x] = y
        ran = counts.values()
        return len(ran) == len(set(ran))

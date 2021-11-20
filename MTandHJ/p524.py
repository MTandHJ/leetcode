


from typing import List
from base import version


class Solution:

    @version("naive")
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def check(item):
            first, second = len(s) - 1, len(item) - 1
            while second >= 0:
                if first < 0:
                    return False
                if s[first] == item[second]:
                    second -= 1
                first -= 1
            return True
        dictionary.sort()
        dictionary.sort(key=len, reverse=True)
        for item in dictionary:
            if check(item):
                return item
        return ''

    @version("better preprocessing")
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def check(item):
            first, second = len(s) - 1, len(item) - 1
            while second >= 0:
                if first < 0:
                    return False
                if s[first] == item[second]:
                    second -= 1
                first -= 1
            return True
        dictionary.sort(key=lambda x: (-len(x), x))
        for item in dictionary:
            if check(item):
                return item
        return ''



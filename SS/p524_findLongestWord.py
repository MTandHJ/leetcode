

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(str)
        res = ''
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < n:
                if t[i] == s[j]:
                    i += 1
                j += 1
            
            if i == len(t):
                if len(t) > len(res) and (len(t) == len(res) and t < res):
                    res = t
        return res

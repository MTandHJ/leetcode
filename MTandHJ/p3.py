


from base import *

class Solution:
    """
    >>> test = Solution()
    >>> s = "abcabcbb"
    >>> test.lengthOfLongestSubstring(s)
    3
    >>> s = "bbbbb"
    >>> test.lengthOfLongestSubstring(s)
    1
    >>> s = ""
    >>> test.lengthOfLongestSubstring(s)
    0
    """
    @version("hash: 64ms, 15mb")
    def lengthOfLongestSubstring(self, s: str) -> int:
        couple = dict()
        node = 0
        the_max = -1
        for i, item in enumerate(s):
            idx = couple.get(item, -999)
            couple[item] = i
            if idx >= node:
                tmp = i - node
                node = idx + 1
                the_max = tmp if tmp > the_max else the_max
        if len(s) - node > the_max:
            the_max = len(s) - node
        return the_max
                
if __name__ == "__main__":
    import doctest
    doctest.testmod()
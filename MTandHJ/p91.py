

from typing import List

from base import version


class Solution:

    @version("over time limits")
    def numDecodings(self, s: str) -> int:
        def search(nums):
            if len(nums) == 0:
                return 1
            elif nums[0] == '0':
                return 0
            counts = 0
            for i, num in enumerate(nums[:2], 1):
                if int(nums[:i]) < 27:
                    counts += search(nums[i:])
            return counts
        return search(s)

    @version("32ms, 15mb")
    def numDecodings(self, s: str) -> int:
        x, y = 0, 1
        s = '9' + s
        try:
            for i in range(1, len(s)):
                if s[i] == '0':
                    assert 0 < int(s[i-1]) < 3
                    z = x
                elif s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                    z = y
                else:
                    z = x + y
                x, y = y, z
        except AssertionError:
            return 0
        return y

    @version("28ms, 15mb")
    def numDecodings(self, s: str) -> int:
        x, y, z = 0, 1, 0
        for i in range(len(s)):
            z = 0
            if s[i] != '0':
                z += y
            if i and s[i - 1] != '0' and int(s[i-1:i+1]) <= 26:
                z += x
            x, y = y, z
        return z
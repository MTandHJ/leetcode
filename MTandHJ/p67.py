

from typing import List

from base import version


class Solution:

    @version("52ms, 15mb")
    def addBinary(self, a: str, b: str) -> str:
        a, b = (a, b) if len(a) <= len(b) else (b, a)
        a = '0' * (len(b) - len(a)) + a
        c = ''
        tmp = 0
        for x, y in zip(a[::-1], b[::-1]):
            cur = (int(x) + int(y) + tmp)
            c = str(cur % 2) + c
            tmp = cur // 2
        if tmp == 1:
            c = '1' + c
        return c

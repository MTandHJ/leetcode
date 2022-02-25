

from typing import List

from base import version


class Solution:

    @version("44ms, 14.9mb")
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


    @version("48ms, 15.1mb")
    def addStrings(self, a: str, b: str) -> str:
        a, b = (a, b) if len(a) <= len(b) else (b, a)
        a = '0' * (len(b) - len(a)) + a
        c = ''
        tmp = 0
        for x, y in zip(a[::-1], b[::-1]):
            cur = (int(x) + int(y) + tmp)
            c = str(cur % 10) + c
            tmp = cur // 10
        if tmp != 0:
            c = str(tmp) + c
        return c

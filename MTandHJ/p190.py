

from typing import List

from base import version


class Solution:

    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:][::-1]
        return int(n, 2) << (32 - len(n))
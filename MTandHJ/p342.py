

from base import version


class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        if n & (-n) != n:
            return False
        while n > 1:
            n = n >> 2
        return n == 1


    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and 0xaaaaaaaa & n == 0

    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and 0x55555555 & n == n

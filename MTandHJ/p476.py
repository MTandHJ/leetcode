


class Solution:

    def findComplement(self, num: int) -> int:
        n  = len(bin(num)) - 2
        return ((1 << n) - 1) ^ num
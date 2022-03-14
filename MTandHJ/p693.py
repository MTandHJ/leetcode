

class Solution:

    def hasAlternatingBits(self, n: int) -> bool:
        x = 0xaaaaaaaa
        y = 0x55555555
        z = x ^ n
        if z & -z > n:
            return True
        z = y ^ n
        if z & -z > n:
            return True
        return False

    def hasAlternatingBits(self, n: int) -> bool:
        k = 1 if n & 1 else 2
        while n:
            if n & 3 != k:
                return False
            n = n >> 2
        return True



test = Solution()

test.hasAlternatingBits(4)
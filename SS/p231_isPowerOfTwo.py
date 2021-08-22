

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n & (n - 1) 是判断最后一位是否为1
        return n > 0 and n & (n - 1)
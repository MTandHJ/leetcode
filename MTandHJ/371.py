

class Solution:

    def getSum(self, a: int, b: int) -> int:
        MAX = 0xffffffff + 1
        while a & b:
            print(a & b)
            a, b = (a & b) << 1, a ^ b
            a %= MAX
            b %= MAX
        return (a | b) % MAX


test = Solution()
print(test.getSum(1, -1))



class Solution:
    def myPow(self, x: float, n: int):
        def quickMul(x: float, n: int):
            if n == 0:
                return 1
            y = quickMul(x, n // 2)
            if n % 2 == 1:
                return y * y
            else:
                return x * y * y
        
        if n >= 0:
            return quickMul(x, n)
        else:
            return 1 / quickMul(x, -n)

ins = Solution()
print(ins.myPow(2, 4))
print(ins.myPow(2, -4))
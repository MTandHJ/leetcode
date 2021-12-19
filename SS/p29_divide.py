

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        def div(a: int, b: int) -> int:
            if a < b:
                return 0
            cnt = 1
            tb = b
            while (tb + tb) <= a:
                cnt = cnt + cnt
                tb = tb + tb
            return cnt + div(a - tb, b)
        
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        
        CONST = 2 ** 31
        INT_MAX = CONST - 1
        INT_MIN = - CONST
        if divisor == -1:
            if dividend > INT_MIN:
                return -dividend
            return INT_MAX
        a = dividend 
        b = divisor
        sign = 1
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            sign = -1
        a = a if a > 0 else -a
        b = b if b > 0 else -b

        res = div(a, b)
        if sign > 0:
            return INT_MAX if res > INT_MAX else res
        return -res

ins = Solution()
print(ins.divide(10, 3))

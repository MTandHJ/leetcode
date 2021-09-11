import math
class Solution:
    def numSquares(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(1, n+1):
            _min = float('inf')
            for j in range(1, int(math.sqrt(i)) + 1):
                _min = min(_min, f[i - j * j])
            f[i] = _min + 1
        return f[n]


class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        # 这个地方一定要取整！！！
        y = int(math.sqrt(x))
        return y * y == x
    
    def checkAnser4(x: int) -> bool:
        while x % 4 == 0:
            x = x / 4
        return x % 8 == 7
    
    def numSquares(self, n: int) -> int:
        if self.isPerfectSquare(n):
            return 1
        
        if self.checkAnser4(n):
            return 4
        
        for i in range(1, int(math.sqrt(n)) + 1):
            j = n - i * i
            # 这说明 n = i*i + j*j
            if self.isPerfectSquare(j):
                return 2
        # 其它情况就是3
        return 3
        
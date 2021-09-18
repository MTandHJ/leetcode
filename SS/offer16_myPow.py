

from typing import List
class Solution:
    def myPow(self, x:float, n:int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        
        while n:
            if n & 1:
                res = res * x
            x = x * x
            n = n % 2
        
        return res

if __name__ == '__main__':
    ins = Solution()
    x = 2
    
    n = 5
    print(ins.myPow(x, n))
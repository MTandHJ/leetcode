


from typing import List
class Solution:
    def hammingWeight(self, n:int) -> int:
        ret = 0
        for i in range(32):
            if n & 1 << i:
                ret += 1
        return ret

class Solution:
    # 这个速度更快，因为在n = n & (n-1)，n是不断减小的，比较的不未0的位数就越来越小
    def hammingWeight(self, n:int) -> int:
        ret = 0
        while n:
            n = n & (n-1)
            ret += 1
        return ret

class Solution:
    def hammingWeight(self, n:int) -> int:
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res
if __name__ == '__main__':
    ins = Solution()
    n = 21
    print(ins.hammingWeight(n))
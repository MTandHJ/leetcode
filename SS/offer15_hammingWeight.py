class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n = n & n-1
            ret += 1
        return ret

if __name__ == '__main__':
    ins = Solution()
    a = 11
    print('final: ', ins.hammingWeight(11))
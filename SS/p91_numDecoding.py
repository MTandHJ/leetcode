class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n+1):
            if s[i-1] != '0':
                f[i] += f[i-1]
            if i > 1 and 10 * int(s[i-2]) + int(s[i-1]) <= 26:
                f[i] += f[i-2]
        return f[-1]
    
    def numDecodings(self, s: str) -> int:
        n = len(s)
        p1, p2 = 0, 1
        for i in range(1, n + 1):
            p3 = 0
            if s[i-1] != '0':
                p3 += p1
            if i > 1 and 10 * int(s[i-2]) + int(s[i-1]) <= 26:
                p3 += p2
            p1, p2 = p2, p3
        return p3

ins = Solution()
s = '226'
print(ins.numDecodings(s))

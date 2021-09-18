class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        for i in range(2, n+1):
            # tmp = [0] * (i-1)
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
            # dp[i] = max(tmp)
        
        return dp[n]

if __name__ == '__main__':
    ins = Solution()
    n = 10
    print(ins.integerBreak(n)

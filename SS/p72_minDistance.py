

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        if not m:
            return n
        if not n:
            return m
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j
        
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]

    def minDistance2(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        if not m:
            return n
        if not n:
            return m
        # 截至第i-1, j-1,所需要变换的次数
        dp = [[0]*(m+1) for _ in range(n+1)]

        # 从0个元素变换到0，1，2，... n个元素需要多少步骤
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                # 说明前面的字符也都相等，
                # dp[i][j] 代表前面的word[0:i], word2[0:j] 
                # 中的最后word1[i-1]=word[j-1] 
                # 变换次数就取决于前面的dp[i][j] 这次新的不用再变换
                
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 这一步肯定是要变换的，所以先加上1
                    # dp[i-1][j-1] += 1
                    # dp[i][j] = 1 + min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1]))
                    # d[i-1][j-1]: 替换
                    # dp[i-1][j] 代表填补
                    # dp[i][j-1] 代表删除
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        return dp[n][m]

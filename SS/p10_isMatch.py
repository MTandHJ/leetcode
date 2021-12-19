

class Solution:
    def isMatch(self, s:str, p:str) -> bool:
        memo = [[-1 for _ in range(len(p))] for _ in range(len(s) + 1)]

        def dfs(i, j):
            # 全部扫描完
            if j == len(p):
                return i == len(s)
            # 如果出现过，直接返回55
            if memo[i][j] != -1:
                return memo[i][j]
            # 当前p[j] 和s[i] 匹配， 两种情况，s[i], '.'
            matchable = i < len(s) and p[j] in {s[i], '.'}

            # 以下都是看后面的是否匹配的
            # j 还没有扫描完，且j向后扫描是万金油，匹配一次或者0次
            if j + 1 < len(p) and p[j +1] == '*':
                memo[i][j] = (matchable and dfs(i + 1, j)) or dfs(i, j + 2)
            else:
                # 当前匹配，后面的也匹配
                memo[i][j] == matchable and dfs(i + 1, j + 1)
            return memo[i][j]
        
        return dfs(0, 0)

class Solution:
    def isMatch(self, s: str, p:str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 判断s[:i], p[:j]最后一个元素是否匹配
        def matchs(i, j):
            if j == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]
        
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j-1] != '*':
                    if matchs(i, j):
                        dp[i][j] = dp[i-1][j-1]
                else:
                    # 判断p的前一个元素是否跟s[:i]的最后一个元素匹配
                    if matchs(i, j-1):
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]
    
    def isMatch2(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        def matchs(i, j):
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]
        
        f = [[False] * n for _ in range(m)]
        f[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if p[j] == '*':
                    f[i][j] |= f[i][j-2]
                    if matchs(i, j):
                        f[i][j] |= f[i-1][j]
                else:
                    if matchs(i, j):
                        f[i][j] |= f[i-1][j-1]
                    else:
                        f[i][j] = False
        return f[-1][-1]

s, p = 'aa', 'a'
s2, p2 = 'aa', 'a*'
ins = Solution()
print(ins.isMatch(s, p))
print(ins.isMatch(s2, p2))
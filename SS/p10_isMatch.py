

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
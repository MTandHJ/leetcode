
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def valid(s):
            bal = 0
            for c in s:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0
        
        self.res = -float('inf')
        def dfs(s, l, r):
            print(l, r)
            if l == r:
                return 0
            if valid(s[l:r]):
                self.res = max(self.res, r - l)
                return self.res
            left = dfs(s, l + 1, r)
            right = dfs(s, l, r - 1)
            self.res = max(self.res, max(left, right))
            return self.res
        
        dfs(0, 0, len(s))
    
    def longestValidParentheses2(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        maxVal = -float('inf')
        dp = [0] * n
        # 第i个元素表示以i为下标的元素的最长字符串长度
        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
            if s[i] == ')':
                if s[i-1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                if s[i-1] == ')' and s[i - dp[i-1] - 1] == '(':
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] = dp[i-1] + dp[i - dp[i-1] + 2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
            maxVal = max(maxVal, dp[i])
        return maxVal

ins = Solution()
print(ins.longestValidParentheses2('(()'))
print(ins.longestValidParentheses2(')()())'))
print(ins.longestValidParentheses2(''))





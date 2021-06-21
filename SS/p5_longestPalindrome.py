from typing import List

class Solution:
    def isPalindromic(self, s):
        length = len(s)
        for i in range(length/2):
            if s[i] != s[length-i-1]:
                return False
        
        return True
    
    def longestPalindrome(self, s):
        max_len = 0
        ans = ''
        length = len(s)
        for i in range(length):
            for j in range(i+1, length+1):
                test = s[i:j]
                if self.isPalindromic(test) and len(test) > max_len:
                    ans = s[i:j]
                    max_len = max(max_len, len(ans))

        return ans

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

class Solution:
    def longestPalindrome(self, s:str) -> bool:
        # 边界条件
        n = len(s)
        if n < 2:
            return True
        
        max_len = 1
        begin = 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 长度
        for L in range(2, n+1):
            # 起始：左边界
            for i in range(n):
                # 右边界
                j = L + i - 1
                # 不能超过s的右边界
                if j >= n:
                    break
                # 左边界 ！= 右边界
                # 这就不可能是回文字符串
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # 包含长度为3的情况
                    # 长度比较短的
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        # 长度比较长的
                        dp[i][j] = dp[i+1][j-1]
                # 在每个循环中
                # 更新长度
                # 更新起点（左边界）
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
            
        return s[begin: begin + max_len]

class Solution:
    def longestPalindrome(self, s:str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        begin = 0
        max_len = 1

        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for L in range(2, n+1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
            
        return s[begin:begin + max_len]

if __name__ == "__main__":
    ins = Solution()
    s = 'abababa'
    print(ins.longestPalindrome(s))

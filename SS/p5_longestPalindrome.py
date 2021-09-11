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


class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 开始扩展
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s:str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        # 最后要包含start, end
        return s[start: end + 1]
        pass
if __name__ == "__main__":
    ins = Solution()
    s = 'abababa'
    print(ins.longestPalindrome(s))


class Solution:
    def longestPalindrome(self, s:str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        # 判断s[i...j]是否是回文子串
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        # 枚举字串的长度
        for l in range(2, n+1):
            # 枚举左边界，左边界的上线刻意设置宽松一些
            for i in range(n):
                # 由于l和i刻意确定右边界
                # j - i + 1 = l
                j = l + i - 1
                # 如果右边界越界，可以退出当前循环
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

    def longestPalindrome(self, s: str):
        res = ''
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2

        return res
    
    def palindrome(self, s: str, l:int, r:int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r+1]
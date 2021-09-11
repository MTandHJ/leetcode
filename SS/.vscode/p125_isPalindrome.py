

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            # 是非字母的
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # 字母的
            if l < r:
                if s[l].lower() != s[r].lower():
                    return False
                l, r = l + 1, r - 1
        return False
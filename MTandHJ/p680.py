

from typing import List
from base import version

class Solution:

    def isPalidrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
 
    @version("tracky")
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if self.isPalidrome(s[left+1:right+1]) or self.isPalidrome(s[left:right]):
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True

    @version("official")
    def validPalindrome(self, s:str) -> bool:
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return check(left + 1, right) or check(left, right - 1)
        return True

    @version("omit")
    def validPalindrome(self, s:str) -> bool:
        if s == s[::-1]:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                a = s[left:right]
                b = s[left+1:right+1]
                return  a == a[::-1] or b == b[::-1]
        return True


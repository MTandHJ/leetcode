

from base import version


class Solution:

    @version("44ms, 14.9mb")
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

    @version("88ms, 14.9mb")
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x = x // 10
        return x == y or x == y // 10

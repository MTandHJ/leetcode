

from typing import List
from base import version


class Solution:
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    @version('complicate')
    def reverseVowels(self, s: str) -> str:
        length = len(s)
        s = list(s)
        left, right = 0, length - 1
        while left < right:
            lt = s[left]
            rt = s[right]

            if lt not in self.vowels:
                left += 1
            if rt not in self.vowels:
                right -= 1
            if (lt in self.vowels) and (rt in self.vowels):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


solver = Solution()

print(solver.reverseVowels('hello'))


from sys import api_version
from typing import List
class Solution:
    def isValid(self, s:str) -> bool:
        n = len(s)
        if not n % 2:
            return False

        pairs = {
            ')': '(',
            '}': '{',
            '[': ']'
        }

        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        print('what a fuck?????')
        return  stack


if __name__ == '__main__':
    ins = Solution()
    s = '()'
    print(ins.isValid(s))
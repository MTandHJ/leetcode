

from base import version

class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for item in s:
            try:
                if item in [')', ']', '}']:
                    assert stack.pop() == mapping[item]
                else:
                    stack.append(item)
            except (IndexError, AssertionError):
                return False
        if len(stack):
            return False
        else:
            return True

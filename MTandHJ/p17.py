

from typing import List

from base import version


class Solution:

    mapping = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    @version("40ms, 15.1mb")
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        def search(start, digits):
            if len(digits) == 0:
                return [start]
            elif len(digits) == 1:
                return [start + item for item in self.mapping[digits[0]]]
            ans = []
            for letter in self.mapping[digits[0]]:
                for item in search(letter, digits[1:]):
                    ans.append(start + item)
            return ans
        return search('', digits)

    @version("36ms, 15.1mb")
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        ans = ['']
        for digit in digits:
            ans = [prev + cur for prev in ans for cur in self.mapping[digit]]
        return ans
            
        


from typing import List

from base import version


class Solution:

    @version("44ms, 14.9mb")
    def convertToTitle(self, columnNumber: int) -> str:
        columnNumber -= 1
        ans = ''
        while columnNumber > 25:
            ans += chr(columnNumber % 26 + ord('A'))
            columnNumber = columnNumber // 26 - 1
        ans += chr(columnNumber + ord('A'))
        return ans[::-1]




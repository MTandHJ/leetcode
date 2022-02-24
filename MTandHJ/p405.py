

from typing import List

from base import version

class Solution:

    mapps = '0123456789abcdef'

    def toHex(self, num: int) -> str:
        items = []
        for k in range(8):
            items.append(num & 15)
            num = num >> 4
            if not num: break
        ans = '' 
        for item in items[::-1]:
            ans += self.mapps[item]
        return ans

    
test = Solution()
test.toHex(12)
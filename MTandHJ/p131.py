

from typing import List

from base import version


class Solution:

    @version("160ms, 28.1mb")
    def partition(self, s: str) -> List[List[str]]:
        def search(cur):
            if cur == len(s):
                return [[]]
            ans = []
            for i in range(cur + 1, len(s) + 1):
                fragment = s[cur:i]
                if fragment == fragment[::-1]:
                    for item in search(i):
                        ans.append([fragment] + item)
            return ans
        return search(0)
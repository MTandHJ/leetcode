

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        occ = set()
        n = len(s)

        rk, ans = -1, 0
        for i in range(n):
            if i:
                occ.remove(s[i-1])
            while rk + 1 < n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, rk -i + 1)
        
        return ans


class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        occ = set()
        ans = 0
        rk, cur = -1, set()
        
        for i in range(n):
            if i:
                cur.remove(s[i-1])
            while rk + 1 < n and s[rk + 1] not in cur:
                cur.add(s[rk+1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans

    def lengthOfLongestSubstring3(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[i])
                left += 1
                cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len
            
if __name__ == "__main__":
    ins = Solution()
    s = 'abcabcbb'
    print(ins.lengthOfLongestSubstring(s))
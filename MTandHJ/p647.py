


from base import version

import collections

class Solution:

    @version("516ms, 14.8mb")
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for left in range(len(s)):
            right = left
            sub = s[left:right+1]
            while True:
                if sub == sub[::-1]:
                    ans += 1
                right += 1
                if right == len(s):
                    break
                sub = s[left:right+1]
        return ans


    def countSubstrings(self, s: str) -> int:
        memory = collections.defaultdict(collections.deque)
        for left, item in enumerate(s):
            memory[item].append(left)
        ans = 0
        for item in s:
            left = memory[item].popleft()
            ans += 1
            for right in memory[item]:
                sub = s[left:right+1]
                if sub == sub[::-1]:
                    ans += 1
        return ans

    @version("44ms, 15.1mb")
    def countSubstrings(self, s: str) -> int:
        s = '.' + '.'.join(s) + '.'
        triple = (0, 0, 0) # center, radius, right
        infos = []
        for center in range(len(s)):
            left = right = center
            if center < triple[-1]:
                j = 2 * triple[0] - center
                radius = min(infos[j], triple[-1] - center + 1)
                left = center - radius + 1
                right = center + radius - 1
            while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1
            infos.append(right - center + 1)
            if right > triple[-1]:
                triple = (center, infos[-1], right)
        ans = 0
        for radius in infos:
            ans += radius // 2
        return ans


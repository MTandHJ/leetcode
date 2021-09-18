
from collections import Counter

class Solution:
    def checkInclusion(self, s1:str, s2:str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        # 对特殊情况判断
        if n2 < n1:
            return False
        # 记录下s1中每个字符出现的次数，这是一个字典
        c1 = Counter(s1)
        # 以窗口为n1，开始滑动
        l, r = 0, n1-1
        while r < n2:
            c2 = Counter(s2[l:r+1])
            # 说明匹配上了
            if c1 == c2:
                return True
            l += 1
            r += 1
        
        return False

class Solution:
    def checkInclusion(self, s1:str, s2:str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        # 因为有26个字母，他们的ASCII值之差在0-25
        cnt = [0] * 26
        for i in range(n1):
            cnt[ord(s1[i]) - 'a'] -= 1
            cnt[ord(s2[i]) - 'a'] += 1
        
        diff = 0
        for val in cnt:
            if val != 0:
                diff += 1
        
        if diff == 0:
            return True
        
        for i in range(n1, n2):
            x = s2[i] - 'a'
            y = s2[i-n1] - 'a'
            if x == y:
                continue
            
            if cnt[x] == 0:
                diff += 1
            cnt[x] += 1
            if cnt[x] == 0:
                diff -= 1
            if cnt[y] == 0:
                diff += 1
            cnt[y] -= 1
            if cnt[y] == 0:
                diff -= 1
            
            if diff == 0:
                return True
        
        return False



class Solution:
    def checkInclusion(self, s1:str, s2:str) -> bool:
        cnt1, cnt2 = [0] * 26, [0] * 26
        n1, n2 = len(s1), len(s2)
        base = ord('a')
        
        if n1 > n2:
            return False
        
        for i in range(n1):
            cnt1[ord(s1[i]) - base] += 1
            cnt2[ord(s2[i]) - base] += 1
        
        for i in range(n1, n2):
            if cnt1 == cnt2:
                return True
            cnt2[ord(s2[i]) - base] += 1
            cnt2[ord(s2[i-n1]) - base] -= 1
        
        return cnt1 == cnt2
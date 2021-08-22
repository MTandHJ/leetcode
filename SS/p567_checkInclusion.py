
from collections import Counter
class Solution:
    def checkInclusion(self, s1:str, s2:str) -> bool:
        count1, count2 = s1.Counter(), s1.Counter()

        N = len(s2)
        start = 0

        left, right = 0, len(s1) - 1
        count2 = Counter(s2[0:right])
        while right < N:
            count2[s2[right]] += 1
            if count1 == count2:
                return True
            
            count2[s2[left]] -= 1
            if count2[s2[left]] == 0:
                del count2[s2[left]]
            
            left += 1
            right += 1
    
        return False

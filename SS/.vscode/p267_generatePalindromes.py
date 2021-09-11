from typing import Collection


from typing import List
import collections

class Solution:
    def generatePalindromes(self, s):
        self.hashmap = collections.Counter(s)
        self.odd = 0
        self.res = []
        for count in self.hashmap.values():
            if count % 2 == 1:
                self.odd += 1
        
        if self.odd > 1:
            return []

        cur = ''
        for key in self.hashmap:
            if self.hashmap[key] % 2 == 1:
                cur += key
                self.hashmap[key] -= 1
        
        self.backtrack(cur, len(s))
        return self.res
    
    def backtrack(self, cur, n):
        if len(cur) > n:
            return 
        if len(cur) == n:
            self.res.append(cur)
        
        for key in self.hashmap:
            if self.hashmap[key] > 1:
                self.hashmap[key] -= 2
                self.backtrack(key + cur + key, n)
                self.hashmap[key] += 2
        
        return

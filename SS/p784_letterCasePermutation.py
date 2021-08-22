

from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[int]:
        res = [[]]
        
        for char in s:
            n = len(s)
            if s.isalpha():
                for i in range(n):
                    res.append(res[i][:])
                    res[i].append(char.lower())
                    res[n+i].append(char.upper())
            else:
                for i in range(n):
                    res.append(char)
        
        return map("".join, res)

class Solution:
    def letterCasePermutation(self, s: str) -> List[int]:

        def dfs(s, n, res):
            if len(s) == n:
                
                return res.append(s)
            if s[n].isalpha():
                return dfs(s, n+1, res)
            
            dfs(s, n+1, res)
            s

class Solution:
    def letterCasePermutation(self, s: str) -> List[int]:
        n = len(s)
        def dfs(path, idx):
            if idx == n:
                res.append(path)
                return
            
            if s[idx].isalpha():
                if s[idx].islower():
                    dfs(path+s[idx].upper(), idx+1)
                if s[idx].isupper():
                    path(path+s[idx].lower(), idx+1)
            else:
                dfs(path + s[idx], idx + 1)
            
            dfs(path + s[idx], idx + 1)

        res = []
        dfs('', 0)
        return res
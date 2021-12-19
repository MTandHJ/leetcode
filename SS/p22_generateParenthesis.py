
from typing import List
from functools import lru_cache

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        
        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0
        
        ans = []
        generate([])
        return ans
    
    def  generateParenthesis2(self, n: int) -> List[int]:
        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    return ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        
        ans = []
        generate('')
        return ans
    
    def generateParenthesis3(self, n: int) -> List[int]:
        ans = []
        def valid(S):
            bal = 0
            for c in S:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        def backtrack(S, l, r):
            if len(S) == 2 * n:
                # 在送入ans之前需要先判断
                if valid(S):
                    ans.append(''.join(S))
                return 
            # 两种
            if l < n:
                if r == n:
                    return 
                S.append('(')
                backtrack(S, l+1, r)
                S.pop()
            if r < n:
                S.append(')')
                backtrack(S, l, r+1)
                S.pop()
        backtrack([], 0, 0)
        return ans

    def generateParenthesis4(self, n: int) -> str:
        combinations = []
        
        def valid(current: str) -> bool:
            bal = 0
            for c in current:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        def generateAll(current: str, pos: int, result: List[str]):
            if pos == len(current):
                if valid(current):
                    result.append(''.join(current))
            else:
                current[pos] = '('
                generateAll(current, pos + 1, result)
                current[pos] = ')'
                generateAll(current, pos + 1, result)
    
    def generateParenthesis5(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, l, r):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return 
            if l < n:
                S.append('(')
                backtrack(S, l + 1, r)
                S.pop()
            if r < n:
                S.append(')')
                backtrack(S, l, r + 1)
                S.pop()

        backtrack('', 0, 0)
        return ans

    @lru_cache(None)
    def generateParenthesis6(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        
        for c in range(n):
            for left in self.generateParenthesis6(c):
                for right in self.generateParenthesis6(n - 1 - c):
                    ans.append('(' + left + ')' + right)
        return ans
            

        



            
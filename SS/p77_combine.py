

from typing import List
class Solution:
    def combine(self, n: int, k:int) -> List[List[int]]:
        res = []

        def backtrack(n, k, start, li):
            if k == 0:
                res.append(li[:])
                return
            for i in range(start, n-k+1):
                li.append(i+1)
                backtrack(n, k-1, i+1, li)
                li.pop()
        backtrack(n, k, 0, [])
        return res

class Solution:
    def combine(self, n: int, k:int) -> List[List[int]]:
        path = []
        res = []
        def backtrack(n, k, start):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                print(path)
                backtrack(n, k, i+1)
                path.pop()
                print(path)
        backtrack(n, k, 1)
        return res


if __name__ == "__main__":
    ins = Solution()
    n, k = 4, 2
    print(ins.combine(n, k))
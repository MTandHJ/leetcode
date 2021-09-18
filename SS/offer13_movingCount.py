from typing import List

class Solution:
    def movingCount(self, m:int, n:int, k:int) -> int:

        def digitSum(n: int) -> int:
            res = 0
            while n:
                res += n % 10
                n = n // 10
            
            return res

        from queue import Queue
        # q = Queue()
        q = []
        # q.put((0, 0))
        q.append((0, 0))
        s = set()

        # while not q.empty():
        while q:
            # x, y = q.get()
            x, y = q.pop(0)
            if (x, y) not in s \
                and 0 <= x < m \
                    and 0 <= y < n \
                        and digitSum(x) + digitSum(y) <= k:
                        s.add((x, y))
                        for nx, ny in [(x+1, y), (x, y+1)]:
                            # 下方 右方
                            # q.put((nx, ny))
                            q.append((nx, ny))
        
        return len(s)


class Solution:
    def movingCount(self, m:int, n:int, k:int) -> int:
        def digitSum(n:int) -> int:
            res = 0
            while n:
                res += n % 10
                n = n // 10
            return res
        
        q = [(0, 0)]
        res = set()
        while q:
            x, y = q.pop(0)
            if (x, y) not in res \
                and 0 <= x < m \
                    and 0 <= y < n \
                        and digitSum(x) + digitSum(y) <= k:
                        res.add((x, y))
                        for i, j in [(x+1, y), (x, y+1)]:
                            q.append((i, j))

        return len(res)


if __name__ == "__main__":
    ins = Solution()
    m, n = 5, 5
    k = 5
    print(ins.movingCount(m, n, k))

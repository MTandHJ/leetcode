

class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        N = len(A)

        ans = cur = None
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        
        rsum = [None] * N
        rsum[-1] = A[-1]
k
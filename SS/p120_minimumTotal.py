

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)
        dp = [[0] * len(triangle[i]) for i in range(depth)]

        if depth < 2:
            return sum(triangle[0])

        dp[0][0] = triangle[0][0]
        for i in range(depth-1):
            for j in range(len(triangle[i]) - 1):
                dp[i][j] = triangle[i][j] + min(triangle[i+1][j:j+2])
        
        return min(dp[depth-1])

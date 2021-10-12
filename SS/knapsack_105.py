

from typing import List


def knapsack(W: int, N: int, weights: List[int], values: List[int]) -> int:
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        w = weights[i-1]
        v = values[i-1]
        j = 1
        while j <= W:
            if j >= w:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else:
                dp[i][j] = dp[i-1][j]
            j += 1
    return dp[-1][-1]

# 不使用矩阵
# 使用一个数组来节省空间
def knapsack2(W: int, N: int, weights: List[int], values: List[int]) -> int:
    dp = [0] * (W + 1)
    for i in range(1, N + 1):
        w = weights[i-1]
        v = values[i-1]
        for j in range(W, 0, -1):
            if j >= w:
                dp[j] = max(dp[j], dp[j-w]) + v
    return dp[-1]
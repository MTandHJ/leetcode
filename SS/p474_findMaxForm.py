

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int):
        length = len(strs)
        dp = [[[0] * (n + 1)] * (m + 1) for _ in range(length + 1)]
        for i in range(1, length + 1):
            zeroOnes = self.getZerosOnes(strs[i-1])
            zeros, ones = zeroOnes
            for j in range(m + 1):
                for k in range(n + 1):
                    # 在这里要先继承上一行的数量
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= zeros and k >= ones:
                        # 这里不要忘记加1，因为是在上一行的基础上加一
                        dp[i][j][k] = max(
                            dp[i-1][j][k],
                            dp[i-1][j-zeros][k-ones]
                        ) + 1
        return dp[-1][-1][-1]

    def getZerosOnes(self, s: str):
        # 获得字符串中0，1 的数量
        zerosOnes = [0] * 2
        length = len(s)
        for i in range(length):
            zerosOnes[int(s(i)) - int('0')] += 1
        return zerosOnes
    

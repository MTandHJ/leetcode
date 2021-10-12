

class Solution:
    def minSteps(self, n: int) -> int:
        if not n:
            return n
        
        # f[i] 代表得到i个A，需要多少次动作
        # 其中f[0], f[1]已经确定
        f = [0] * (n + 1)
        j = 1
        # res = 0
        for i in range(2, n):
            j = 1
            # 但是f[2], f[3]就没确定
            f[i] = float('inf')
            while j * j <= i:
                f[i] = min(f[i], f[i] + i // j)
                f[i] = min(f[i], f[i // j] + j)
                j += 1
        return f[-1]
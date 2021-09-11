
import numpy as np
# import pandas as pd
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        res = 0

        l0, l = 0, 0 
        r = n - 1
        while l < r:
            while text[l] != text[r]:
                l += 1
            if l == r:
                res += 1
                return res
            elif l < r:
                word_len = l - l0 + 1
                if text[l0: l+1] == text[r-word_len+1, r+1]:
                    res += 2
                    l += 1
                    l0 = l
                    r -= word_len
                else:
                    l += 1

            elif l > r:
                break
        return res


class Solution:
    def longestDecomposition(self, text: str):
        return self.divide(text, 0)
    
    def divide(self, text: str, n: int) -> int:
        m = len(text)
        # 前面和后面一一对应，中间没有“单个”元素
        if not text:
            return n
        # 进行递归
        for i in range(m / 2):
            if text[:i+1] == text[m-i-1:m]:
                return self.divide(text[i+1:m-i-1], n+2)
        # 最后只剩下一个元素
        return n + 1


from typing import List

from functools import reduce

class Solution:

    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        for i, word1 in enumerate(words):
            for word2 in words[i:]:
                if len(set(word1 + word2)) == len(set(word1)) + len(set(word2)):
                    cur = len(word1) * len(word2)
                    if cur > ans:
                        ans = cur
        return ans


    def maxProduct(self, words: List[str]) -> int:
        masks = [reduce(lambda a, b: a | (1 << ord(b) - ord('a')), word, 0) for word in words]
        ans = 0
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words[i + 1:], i + 1):
                if not masks[i] & masks[j]:
                    cur = len(word1) * len(word2)
                    if cur > ans:
                        ans = cur
        return ans
                    

                    

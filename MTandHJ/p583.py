

from typing import List

from base import version


class Solution:

    @version("over time limits")
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        memory = dict()
        def search(word1, word2, steps):
            if len(word1) < len(word2):
                word1, word2 = word2, word1
            if word2 in memory:
                return memory[word2]
            ans = []
            for i, alpha in enumerate(word1):
                word = word1[:i] + word1[i+1:]
                if word == word2:
                    memory[word] = steps + 1
                    return memory[word]
                else:
                    ans.append(search(word, word2, steps + 1))
            return min(ans)
        return search(word1, word2, 0) 


    def minDistance(self, word1: str, word2: str) -> int:
        def search(word1, word2):
            if word1 == word2:
                return len(word1)
            if not (len(word1) and len(word2)):
                return 0
            if word1[-1] == word2[-1]:
                return search(word1[:-1], word2[:-1]) + 1
            else:
                return max(search(word1, word2[:-1]), search(word1[:-1], word2))
        return len(word1) + len(word2) - search(word1, word2) * 2


    def minDistance(self, word1: str, word2: str) -> int:
        x, y = 0, 0

test = Solution()
test.minDistance('sea', 'eat')
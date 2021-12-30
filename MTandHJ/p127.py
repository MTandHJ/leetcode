


from typing import List

from base import version


class Solution:

    @version("672ms, 15.9mb")
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = len(beginWord)
        wordList = set(wordList)
        wordEle = [set(elements) for elements in zip(*wordList)]
        prev = [beginWord]
        steps = 1
        while prev and wordEle:
            cur = []
            steps += 1
            for candidate in prev:
                for level in range(length):
                    for ele in wordEle[level]:
                        try:
                            word = list(candidate)
                            word[level] = ele
                            word = ''.join(word)
                            wordList.remove(word)
                            if word == endWord:
                                return steps
                            cur.append(word)
                        except KeyError:
                            pass
            prev = cur
            wordEle = [set(elements) for elements in zip(*wordList)]
        return 0

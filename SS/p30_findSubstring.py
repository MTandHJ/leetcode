

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def isEqual(a, b):
            if len(a) != len(b):
                return False
            for key, val in a.items():
                if b[key] != val:
                    return False
            return True

        if not s or not words:
            return []
        
        n = len(s)
        all_len = 0
        for word in words:
            all_len += len(word)
        
        counts = Counter(words)
        res = []
        i = 0
        while i < n - all_len + 1:
            cur = s[i: i + all_len]
            flag = True
            d = {}
            for word in words:
                print(i, cur)
                if word not in cur:
                    i += 1
                    flag = False
                    # break
                elif word in cur:
                    cur = cur.replace(word, '', 1)
                    print(word)
                    if word not in d:
                        # print(i)
                        # print('not in', word)
                        d[word] = 1
                    else:
                        # print(i)
                        # print('in', word)
                        d[word] += 1
                if not flag: break
            # print(i, d)
            if isEqual(counts, d) and flag:
                # print(i, s[i: i + all_len])
                # print(counts, d)
                res.append(i)
                i += 1
        return res

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
ins = Solution()
print(ins.findSubstring(s, words))
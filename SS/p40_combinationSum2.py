
import collections
from typing import List, Sequence


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal seq 
            if rest == 0:
                ans.append(seq[:])
                return 
            if pos == len(seq) or rest < freq[pos][0]:
                return 
            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                seq.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            seq = seq[:-most]
        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        seq = list()
        dfs(0, target)
        return ans
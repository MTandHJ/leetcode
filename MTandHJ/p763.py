


from typing import List
from collections import defaultdict

from base import version


class Solution:

    @version("56ms, 15.1mb")
    def partitionLabels(self, s: str) -> List[int]:
        seeds = set(s)
        query = {seed:seed for seed in seeds}
        loc = dict()
        for i, item in enumerate(s):
            start =  loc.get(item, False)
            if start is not None:
                print(set(s[start:i]))
                for node in set(s[start:i]):
                    query[node] = query[item]
            loc[item] = i
        count = []
        prev = ''
        for item in s:
            if query[item] != prev:
                count.append(1)
                prev = query[item]
            else:
                count[-1] += 1
        return count

    @version("40ms, 15mb")
    def partitionLabels(self, s: str) -> List[int]:
        loc = dict()
        for i, item in enumerate(s):
            if loc.get(item, None) is None:
                loc[item] = [i, i]
            else:
                loc[item][1] = i
        intervals = list(loc.values())
        count = [0]
        mark = intervals[0][1]
        for inter in intervals:
            if inter[0] > mark:
                count[-1] = mark - count[-1] + 1
                count.append(mark + 1)
            mark = max(inter[1], mark)
        count[-1] = mark - count[-1] + 1
        return count

    @version("40ms, 15mb")
    def partitionLabels(self, s: str) -> List[int]:
        loc = dict()
        for i, item in enumerate(s):
            loc[item] = i
        start, end = 0, 0
        counts = []
        for i, item in enumerate(s):
            end = max(loc[item], end)
            if i == end:
                counts.append(end - start + 1)
                start = end + 1
        return counts
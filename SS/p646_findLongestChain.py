
from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curMax, ans = -float('inf'), 0
        # 与第一个对的第一个元素进行对比
        # NOTE: 这里的curMax 不会和第二个元素Y比较，所以，只记录满足条件的一对对
        for x, y in pairs:
            if curMax < x:
                curMax = y
                ans += 1
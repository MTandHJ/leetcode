from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 存储已经合并的集合
        merged = []

        # 遍历所有的集合，找到所有相交的集合
        for li in intervals:
            # (a, b) (c, d) 
            # b < c -> 没有交集
            # 其他则说明有交集
            if not merged or merged[-1][1] < li[0]:
                merged.append(li)
            else:
                # 上一个合并的a肯定是最小的一个下界，
                # 但是上界, 就需要从已经合并 & 新的(遍历的)集合中找
                merged[-1][1] = max(merged[-1][1], li[1])
        
        return merged
"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # stage-1 未考虑交集的顺序
        # 我首先想到的还是哈希表，将其转化为字典
        def to_dict(nums):
            d_s = {k:0 for k in set(nums)}
            for num in nums:
                d_s[num] += 1

            return d_s
        d_s_1 = to_dict(nums1)
        d_s_2 = to_dict(nums2)

        # 先把所有的key都拿出来
        union = set(d_s_1.keys()) & set(d_s_2.keys())
        d_s = {k:0 for k in union}

        for k in union:
            try:
                d_s[k] = min(d_s_1[k], d_s_2[k])
            except:
                pass

        tmp = []
        for k in union:
            tmp = tmp + [k] * d_s[k]
        
        return tmp
"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。
"""
import collections
from typing import List
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


# 双指针做法
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 先排序
        nums1.sort()
        nums2.sort()

        # 找出每组的长度
        length1, length2 = len(nums1), len(nums2)
        # 用来放共同的都有的数据，也就是交集
        intersection = list()
        # 初始化指针（原来就是索引！！！
        index1 = index2 = 0
        # 开始遍历循环，直到所有的都遍历完
        # 总是小的index += 1
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                # 他们两个都有，且相等
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1
        
        return intersection

# 作者：demigodliu
# 链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/ha-xi-biao-liang-ge-shu-zu-de-jiao-ji-ii-fkwo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 评论区学习来的
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        nums = count1 & count2
        # 求COunter的交集
        return nums.elements()



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 按照顺序排列
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        # 先找到nums1中的元素
        m = collections.Counter()
        for num in nums1:
            m[num] += 1
        
        # 交集用列表来表示
        intersection = list()
        for num in nums2:
            # 如果在原来的中有nums2中的元素
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                # 删除这个元素
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        
        return intersection
